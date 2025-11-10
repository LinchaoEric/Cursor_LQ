# Wispr Flow Clone

A lightweight reference implementation of Wispr Flow-style bilingual voice capture with streaming transcription powered by OpenAI Whisper.

## Features

- 🎙️ Browser-based audio capture using the MediaRecorder API
- ⚡ Near real-time transcripts by uploading ~4s chunks while recording
- 🌐 FastAPI backend that proxies audio chunks to OpenAI Whisper (`whisper-1` by default)
- 🈳 Automatic English / Chinese detection with optional manual overrides
- 🛡️ CORS enabled so the UI can be served from anywhere if you decouple front/back

## Project layout

```
projects/wispr_flow_clone/
├── backend/          # FastAPI app + OpenAI integration
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
└── frontend/         # Static UI served directly by FastAPI
    ├── index.html
    ├── main.js
    └── styles.css
```

## Setup

1. **Install backend deps**
   ```bash
   cd projects/wispr_flow_clone/backend
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env  # set OPENAI_API_KEY
   ```

2. **Run the FastAPI server**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Open the UI**
   Visit http://localhost:8000/ and grant microphone access. The page is served directly from FastAPI, so no separate frontend build step is needed.

## How live transcription works

- `MediaRecorder` slices microphone audio into small WebM chunks every 4 seconds.
- Each chunk is posted to `/api/transcribe-chunk` as soon as it is ready; uploads happen concurrently.
- FastAPI writes the chunk to a temp file, forwards it to OpenAI Whisper, and streams the transcript text back to the browser.
- The UI appends each chunk’s transcription immediately, giving a near-live experience.

## Customization ideas

- Adjust chunk cadence via `mediaRecorder.start(timeslice)` in `frontend/main.js`.
- Store transcripts server-side (e.g., Postgres) for later retrieval.
- Add speaker labels or translation using OpenAI GPT models after Whisper completes.
- Wrap the backend with authentication if you plan to expose it publicly.

## Notes

- Browsers only grant microphone access over HTTPS or `http://localhost`, so deploy behind TLS.
- OpenAI Whisper automatically detects Chinese vs. English, but the UI’s language selector lets you hint a fixed language when needed.
- `WHISPER_MODEL` can be changed via env var if OpenAI releases improved checkpoints.
