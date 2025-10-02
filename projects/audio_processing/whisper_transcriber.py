import whisper
import json
import os
from datetime import datetime

def transcribe_audio_with_whisper(audio_path, model_size="base"):
    """
    Transcribe audio using OpenAI Whisper
    model_size options: "tiny", "base", "small", "medium", "large"
    """
    try:
        print(f"Loading Whisper model: {model_size}")
        model = whisper.load_model(model_size)
        
        print(f"Transcribing audio file: {audio_path}")
        result = model.transcribe(audio_path)
        
        return result
        
    except Exception as e:
        print(f"Error during transcription: {e}")
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
        "estimated_duration": len(segments) * 30 if segments else 0,  # Rough estimate
        "segments_count": len(segments),
        "language": result.get("language", "unknown"),
        "content_summary": text[:300] + "..." if len(text) > 300 else text,
        "segments": []
    }
    
    # Add segment details
    for i, segment in enumerate(segments[:5]):  # First 5 segments
        analysis["segments"].append({
            "segment_id": i,
            "start": segment.get("start", 0),
            "end": segment.get("end", 0),
            "text": segment.get("text", "").strip(),
            "confidence": segment.get("confidence", 0)
        })
    
    return analysis

def save_results(transcription_result, analysis, output_file="whisper_transcription_results.json"):
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
    # Audio file path
    audio_file = "DoorDash Audio File/New Recording 8.m4a"
    
    print("OpenAI Whisper Audio Transcription Tool")
    print("=" * 50)
    
    # Check if audio file exists
    if not os.path.exists(audio_file):
        print(f"Error: Audio file not found at {audio_file}")
        return
    
    print(f"Audio file found: {audio_file}")
    print(f"File size: {os.path.getsize(audio_file) / (1024*1024):.1f} MB")
    
    # Transcribe with Whisper
    print("\nStarting transcription...")
    result = transcribe_audio_with_whisper(audio_file, model_size="base")
    
    if result:
        print("\n" + "=" * 50)
        print("TRANSCRIPTION COMPLETE")
        print("=" * 50)
        
        # Display transcription
        print("\nTRANSCRIPTION:")
        print("-" * 30)
        print(result["text"])
        
        # Analyze results
        print("\n" + "=" * 50)
        print("CONTENT ANALYSIS")
        print("=" * 50)
        
        analysis = analyze_transcription(result)
        
        print(f"Language: {analysis['language']}")
        print(f"Word Count: {analysis['word_count']}")
        print(f"Character Count: {analysis['character_count']}")
        print(f"Segments: {analysis['segments_count']}")
        print(f"Estimated Duration: {analysis['estimated_duration']:.1f} seconds")
        
        print(f"\nContent Summary:")
        print("-" * 30)
        print(analysis['content_summary'])
        
        # Show first few segments with timestamps
        if analysis['segments']:
            print(f"\nFirst {len(analysis['segments'])} segments:")
            print("-" * 30)
            for segment in analysis['segments']:
                start_time = f"{segment['start']:.1f}s"
                end_time = f"{segment['end']:.1f}s"
                confidence = f"{segment['confidence']:.2f}" if segment['confidence'] else "N/A"
                print(f"[{start_time}-{end_time}] (conf: {confidence})")
                print(f"  {segment['text']}")
                print()
        
        # Save results
        save_results(result, analysis)
        
    else:
        print("Transcription failed. Please check the audio file.")

if __name__ == "__main__":
    main()
