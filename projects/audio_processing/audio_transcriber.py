import speech_recognition as sr
from pydub import AudioSegment
import os
import json

def convert_m4a_to_wav(m4a_path, wav_path):
    """Convert M4A file to WAV format for speech recognition"""
    try:
        audio = AudioSegment.from_file(m4a_path, format="m4a")
        audio.export(wav_path, format="wav")
        print(f"Successfully converted {m4a_path} to {wav_path}")
        return True
    except Exception as e:
        print(f"Error converting audio: {e}")
        return False

def transcribe_audio(audio_path):
    """Transcribe audio file to text using Google Speech Recognition"""
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_path) as source:
            print("Loading audio file...")
            audio = recognizer.record(source)
            
        print("Transcribing audio...")
        text = recognizer.recognize_google(audio)
        return text
        
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from speech recognition service; {e}")
        return None
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

def analyze_audio_content(text):
    """Analyze the transcribed text for key insights"""
    if not text:
        return {}
    
    analysis = {
        "word_count": len(text.split()),
        "character_count": len(text),
        "estimated_duration": len(text.split()) / 150,  # Rough estimate: 150 words per minute
        "sentences": len([s for s in text.split('.') if s.strip()]),
        "content_summary": text[:200] + "..." if len(text) > 200 else text
    }
    
    return analysis

def main():
    # File paths
    m4a_file = "DoorDash Audio File/New Recording 8.m4a"
    wav_file = "temp_audio.wav"
    
    print("Audio Transcription and Analysis Tool")
    print("=" * 40)
    
    # Check if audio file exists
    if not os.path.exists(m4a_file):
        print(f"Error: Audio file not found at {m4a_file}")
        return
    
    # Convert M4A to WAV
    print("Step 1: Converting M4A to WAV format...")
    if not convert_m4a_to_wav(m4a_file, wav_file):
        return
    
    # Transcribe audio
    print("Step 2: Transcribing audio to text...")
    transcribed_text = transcribe_audio(wav_file)
    
    if transcribed_text:
        print("\n" + "=" * 40)
        print("TRANSCRIPTION COMPLETE")
        print("=" * 40)
        print(transcribed_text)
        
        # Analyze the content
        print("\n" + "=" * 40)
        print("CONTENT ANALYSIS")
        print("=" * 40)
        analysis = analyze_audio_content(transcribed_text)
        
        for key, value in analysis.items():
            if key == "estimated_duration":
                print(f"{key.replace('_', ' ').title()}: {value:.1f} minutes")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        # Save results to file
        results = {
            "transcription": transcribed_text,
            "analysis": analysis
        }
        
        with open("transcription_results.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\nResults saved to transcription_results.json")
        
    else:
        print("Transcription failed. Please check the audio file.")
    
    # Clean up temporary file
    if os.path.exists(wav_file):
        os.remove(wav_file)
        print(f"Cleaned up temporary file: {wav_file}")

if __name__ == "__main__":
    main()
