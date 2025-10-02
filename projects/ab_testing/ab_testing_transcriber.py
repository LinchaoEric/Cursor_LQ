import whisper
import json
import os
from datetime import datetime
import re

def transcribe_ab_testing_webinar(audio_path, model_size="base"):
    """
    Transcribe AB Testing webinar using OpenAI Whisper
    """
    try:
        print(f"Loading Whisper model: {model_size}")
        model = whisper.load_model(model_size)
        
        print(f"Transcribing AB Testing webinar: {audio_path}")
        result = model.transcribe(audio_path)
        
        return result
        
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

def extract_ab_testing_key_points(text):
    """
    Extract key points specifically related to AB testing for interview preparation
    """
    key_points = {
        "ab_testing_basics": [],
        "implementation_steps": [],
        "metrics_and_kpis": [],
        "common_pitfalls": [],
        "best_practices": [],
        "technical_considerations": [],
        "interview_tips": []
    }
    
    # Convert to lowercase for easier pattern matching
    text_lower = text.lower()
    sentences = re.split(r'[.!?]+', text)
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        sentence_lower = sentence.lower()
        
        # AB Testing basics
        if any(keyword in sentence_lower for keyword in ['ab test', 'a/b test', 'split test', 'experiment']):
            key_points["ab_testing_basics"].append(sentence)
            
        # Implementation steps
        if any(keyword in sentence_lower for keyword in ['step', 'process', 'implement', 'setup', 'configure']):
            key_points["implementation_steps"].append(sentence)
            
        # Metrics and KPIs
        if any(keyword in sentence_lower for keyword in ['metric', 'kpi', 'conversion', 'revenue', 'click', 'engagement', 'ctr', 'roi']):
            key_points["metrics_and_kpis"].append(sentence)
            
        # Common pitfalls
        if any(keyword in sentence_lower for keyword in ['pitfall', 'mistake', 'error', 'wrong', 'avoid', 'don\'t', 'never']):
            key_points["common_pitfalls"].append(sentence)
            
        # Best practices
        if any(keyword in sentence_lower for keyword in ['best practice', 'should', 'recommend', 'good', 'effective', 'successful']):
            key_points["best_practices"].append(sentence)
            
        # Technical considerations
        if any(keyword in sentence_lower for keyword in ['technical', 'code', 'algorithm', 'statistical', 'significance', 'sample size', 'confidence']):
            key_points["technical_considerations"].append(sentence)
            
        # Interview tips
        if any(keyword in sentence_lower for keyword in ['interview', 'question', 'answer', 'explain', 'describe', 'how would you']):
            key_points["interview_tips"].append(sentence)
    
    return key_points

def create_interview_notes(transcription_result, key_points):
    """
    Create structured interview notes from the transcription
    """
    notes = {
        "title": "AB Testing Webinar - Interview Preparation Notes",
        "date_processed": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": transcription_result.get("text", "")[:500] + "..." if len(transcription_result.get("text", "")) > 500 else transcription_result.get("text", ""),
        "key_points": key_points,
        "full_transcript": transcription_result.get("text", ""),
        "segments": transcription_result.get("segments", [])
    }
    
    return notes

def save_interview_notes(notes, output_file="ab_testing_interview_notes.json"):
    """Save interview notes to JSON file"""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)
    
    print(f"Interview notes saved to {output_file}")

def create_markdown_notes(notes, output_file="AB_Testing_Interview_Notes.md"):
    """Create a markdown file with formatted interview notes"""
    
    markdown_content = f"""# AB Testing Webinar - Interview Preparation Notes

*Generated on: {notes['date_processed']}*

## Summary
{notes['summary']}

## Key Points for Interview Preparation

### 1. AB Testing Basics
"""
    
    for point in notes['key_points']['ab_testing_basics'][:5]:  # Top 5 points
        markdown_content += f"- {point}\n"
    
    markdown_content += """
### 2. Implementation Steps
"""
    
    for point in notes['key_points']['implementation_steps'][:5]:
        markdown_content += f"- {point}\n"
    
    markdown_content += """
### 3. Metrics and KPIs
"""
    
    for point in notes['key_points']['metrics_and_kpis'][:5]:
        markdown_content += f"- {point}\n"
    
    markdown_content += """
### 4. Common Pitfalls to Avoid
"""
    
    for point in notes['key_points']['common_pitfalls'][:5]:
        markdown_content += f"- {point}\n"
    
    markdown_content += """
### 5. Best Practices
"""
    
    for point in notes['key_points']['best_practices'][:5]:
        markdown_content += f"- {point}\n"
    
    markdown_content += """
### 6. Technical Considerations
"""
    
    for point in notes['key_points']['technical_considerations'][:5]:
        markdown_content += f"- {point}\n"
    
    markdown_content += """
### 7. Interview Tips
"""
    
    for point in notes['key_points']['interview_tips'][:5]:
        markdown_content += f"- {point}\n"
    
    markdown_content += """
## Full Transcript
```
"""
    
    markdown_content += notes['full_transcript']
    markdown_content += """
```

---
*Notes generated from AB Testing Webinar audio file*
"""
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print(f"Markdown notes saved to {output_file}")

def main():
    # Audio file path
    audio_file = "AB Testing Webnar.m4a"
    
    print("AB Testing Webinar Transcription Tool")
    print("=" * 50)
    
    # Check if audio file exists
    if not os.path.exists(audio_file):
        print(f"Error: Audio file not found at {audio_file}")
        return
    
    print(f"Audio file found: {audio_file}")
    print(f"File size: {os.path.getsize(audio_file) / (1024*1024):.1f} MB")
    
    # Transcribe with Whisper
    print("\nStarting transcription...")
    result = transcribe_ab_testing_webinar(audio_file, model_size="base")
    
    if result:
        print("\n" + "=" * 50)
        print("TRANSCRIPTION COMPLETE")
        print("=" * 50)
        
        # Extract key points for interview preparation
        print("\nExtracting key points for interview preparation...")
        key_points = extract_ab_testing_key_points(result["text"])
        
        # Create interview notes
        notes = create_interview_notes(result, key_points)
        
        # Save results
        save_interview_notes(notes)
        create_markdown_notes(notes)
        
        # Display summary
        print("\n" + "=" * 50)
        print("INTERVIEW PREPARATION SUMMARY")
        print("=" * 50)
        
        print(f"Total key points extracted:")
        for category, points in key_points.items():
            print(f"  {category.replace('_', ' ').title()}: {len(points)} points")
        
        print(f"\nWord count: {len(result['text'].split())}")
        print(f"Language: {result.get('language', 'unknown')}")
        
        print(f"\nFiles created:")
        print(f"  - ab_testing_interview_notes.json (structured data)")
        print(f"  - AB_Testing_Interview_Notes.md (formatted notes)")
        
    else:
        print("Transcription failed. Please check the audio file.")

if __name__ == "__main__":
    main()
