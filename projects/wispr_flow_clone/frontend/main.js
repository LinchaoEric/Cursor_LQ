const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const statusEl = document.getElementById('status');
const transcriptLog = document.getElementById('transcriptLog');
const languageSelect = document.getElementById('language');

let mediaRecorder;
let stream;
let chunkIndex = 0;
let pendingUploads = 0;
let isRecording = false;

const STATUS = {
  idle: 'Idle',
  recording: 'Recording…',
  uploading: (count) => `Transcribing ${count} chunk${count === 1 ? '' : 's'}…`,
  error: 'Error - check console',
};

function updateStatus(text) {
  statusEl.textContent = text;
}

function appendTranscript(text, chunkId) {
  if (!text) return;
  const entry = document.createElement('div');
  entry.className = 'transcript-entry';

  const timestamp = document.createElement('span');
  timestamp.className = 'timestamp';
  const now = new Date();
  timestamp.textContent = `Chunk ${chunkId} · ${now.toLocaleTimeString()}`;

  const content = document.createElement('div');
  content.className = 'text';
  content.textContent = text;

  entry.appendChild(timestamp);
  entry.appendChild(content);
  transcriptLog.appendChild(entry);
  transcriptLog.scrollTop = transcriptLog.scrollHeight;
}

async function sendChunk(blob, chunkId) {
  const formData = new FormData();
  formData.append('audio', blob, `chunk-${chunkId}.webm`);
  formData.append('chunk_id', chunkId);
  const language = languageSelect.value;
  if (language && language !== 'auto') {
    formData.append('language', language);
  }

  pendingUploads += 1;
  updateStatus(STATUS.uploading(pendingUploads));

  try {
    const response = await fetch('/api/transcribe-chunk', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Backend returned ${response.status}`);
    }

    const payload = await response.json();
    appendTranscript(payload.text, payload.chunkId ?? chunkId);
  } catch (error) {
    console.error('Unable to transcribe chunk', error);
    updateStatus(STATUS.error);
  } finally {
    pendingUploads -= 1;
    if (isRecording) {
      updateStatus(STATUS.recording);
    } else if (pendingUploads > 0) {
      updateStatus(STATUS.uploading(pendingUploads));
    } else {
      updateStatus(STATUS.idle);
    }
  }
}

function setupRecorder() {
  if (!navigator.mediaDevices?.getUserMedia || typeof MediaRecorder === 'undefined') {
    throw new Error('MediaRecorder API not supported in this browser');
  }
}

async function startRecording() {
  if (isRecording) return;

  try {
    setupRecorder();
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
  } catch (error) {
    console.error('Unable to start recording', error);
    updateStatus('Microphone permission denied');
    return;
  }

  chunkIndex = 0;
  isRecording = true;
  transcriptLog.innerHTML = '';

  mediaRecorder.addEventListener('dataavailable', (event) => {
    if (event.data.size > 0) {
      const currentChunkId = `${Date.now()}-${chunkIndex++}`;
      sendChunk(event.data, currentChunkId);
    }
  });

  mediaRecorder.addEventListener('stop', () => {
    stream.getTracks().forEach((track) => track.stop());
  });

  mediaRecorder.start(4000); // send ~4s chunks for near real-time feedback
  startBtn.disabled = true;
  stopBtn.disabled = false;
  updateStatus(STATUS.recording);
}

function stopRecording() {
  if (!isRecording) return;
  isRecording = false;
  mediaRecorder.stop();
  startBtn.disabled = false;
  stopBtn.disabled = true;
  if (pendingUploads === 0) {
    updateStatus(STATUS.idle);
  }
}

startBtn.addEventListener('click', startRecording);
stopBtn.addEventListener('click', stopRecording);

window.addEventListener('beforeunload', () => {
  if (isRecording) {
    stopRecording();
  }
});
