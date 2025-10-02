import os
import json
import subprocess
import sys
from datetime import datetime

def try_whisper_direct(audio_path):
    """Try to use Whisper directly with the audio file"""
    try:
        import whisper
        print("Attempting direct Whisper transcription...")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result
    except Exception as e:
        print(f"Direct Whisper failed: {e}")
        return None

def try_convert_with_system(audio_path):
    """Try to convert audio using system tools"""
    try:
        # Try using afconvert (macOS built-in)
        output_path = "temp_audio.wav"
        cmd = ["afconvert", "-f", "WAVE", "-d", "LEI16@44100", audio_path, output_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Successfully converted audio using afconvert")
            return output_path
        else:
            print(f"afconvert failed: {result.stderr}")
            return None
    except Exception as e:
        print(f"System conversion failed: {e}")
        return None

def transcribe_with_whisper(audio_path):
    """Transcribe using Whisper after conversion"""
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result
    except Exception as e:
        print(f"Whisper transcription failed: {e}")
        return None

def analyze_transcription(result):
    """Analyze the transcription results"""
    if not result:
        return {}
    
    text = result.get("text", "")
    segments = result.get("segments", [])
    
    analysis = {
        "word_count": len(text.split()),
        "character_count": len(text),
        "segments_count": len(segments),
        "language": result.get("language", "unknown"),
        "content_summary": text[:300] + "..." if len(text) > 300 else text,
        "segments": []
    }
    
    # Add segment details
    for i, segment in enumerate(segments[:5]):
        analysis["segments"].append({
            "segment_id": i,
            "start": segment.get("start", 0),
            "end": segment.get("end", 0),
            "text": segment.get("text", "").strip()
        })
    
    return analysis

def save_results(transcription_result, analysis, output_file="transcription_results.json"):
    """Save transcription and analysis results to JSON file"""
    results = {
        "timestamp": datetime.now().isoformat(),
        "transcription": transcription_result,
        "analysis": analysis
    }
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"Results saved to {output_file}")

def main():
    audio_file = "DoorDash Audio File/New Recording 8.m4a"
    
    print("Simple Audio Transcription Tool")
    print("=" * 40)
    
    # Check if audio file exists
    if not os.path.exists(audio_file):
        print(f"Error: Audio file not found at {audio_file}")
        return
    
    print(f"Audio file found: {audio_file}")
    print(f"File size: {os.path.getsize(audio_file) / (1024*1024):.1f} MB")
    
    # Try direct Whisper first
    print("\nMethod 1: Direct Whisper transcription...")
    result = try_whisper_direct(audio_file)
    
    if not result:
        print("\nMethod 2: Converting audio first...")
        converted_path = try_convert_with_system(audio_file)
        
        if converted_path and os.path.exists(converted_path):
            result = transcribe_with_whisper(converted_path)
            
            # Clean up converted file
            os.remove(converted_path)
    
    if result:
        print("\n" + "=" * 40)
        print("TRANSCRIPTION COMPLETE")
        print("=" * 40)
        
        # Display transcription
        print("\nTRANSCRIPTION:")
        print("-" * 30)
        print(result["text"])
        
        # Analyze results
        print("\n" + "=" * 40)
        print("CONTENT ANALYSIS")
        print("=" * 40)
        
        analysis = analyze_transcription(result)
        
        print(f"Language: {analysis['language']}")
        print(f"Word Count: {analysis['word_count']}")
        print(f"Character Count: {analysis['character_count']}")
        print(f"Segments: {analysis['segments_count']}")
        
        print(f"\nContent Summary:")
        print("-" * 30)
        print(analysis['content_summary'])
        
        # Save results
        save_results(result, analysis)
        
    else:
        print("\nAll transcription methods failed.")
        print("Please ensure ffmpeg is installed or try a different audio format.")

if __name__ == "__main__":
    main()
