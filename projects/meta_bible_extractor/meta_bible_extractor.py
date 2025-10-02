#!/usr/bin/env python3
"""
Meta Bible Content Extractor
Extracts text content from Meta Bible images and organizes it into a readable format.
"""

import os
import json
from PIL import Image
import pytesseract
import re

class MetaBibleExtractor:
    def __init__(self, image_dir="Meta Bible"):
        self.image_dir = image_dir
        self.extracted_content = {}
        
    def extract_text_from_image(self, image_path):
        """Extract text from a single image using OCR."""
        try:
            # Open the image
            image = Image.open(image_path)
            
            # Extract text using pytesseract
            text = pytesseract.image_to_string(image)
            
            return text.strip()
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return ""
    
    def process_all_images(self):
        """Process all JPEG images in the Meta Bible directory."""
        jpg_files = [f for f in os.listdir(self.image_dir) if f.endswith('.jpg')]
        jpg_files.sort()  # Sort to maintain order
        
        print(f"Found {len(jpg_files)} JPEG images to process...")
        
        for jpg_file in jpg_files:
            image_path = os.path.join(self.image_dir, jpg_file)
            print(f"Processing {jpg_file}...")
            
            # Extract text from image
            text_content = self.extract_text_from_image(image_path)
            
            if text_content:
                # Store the extracted content
                self.extracted_content[jpg_file] = text_content
                print(f"Successfully extracted text from {jpg_file}")
            else:
                print(f"No text extracted from {jpg_file}")
    
    def organize_content(self):
        """Organize the extracted content into a structured format."""
        organized_content = {
            "overview": {},
            "knowledge_points": [],
            "sample_questions": [],
            "answers": [],
            "raw_content": {}
        }
        
        # Process each image's content
        for image_name, content in self.extracted_content.items():
            # Store raw content
            organized_content["raw_content"][image_name] = content
            
            # Try to identify content type and organize accordingly
            lines = content.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Look for patterns that indicate knowledge points
                if any(keyword in line.lower() for keyword in ['key point', 'knowledge', 'concept', 'principle', 'framework']):
                    organized_content["knowledge_points"].append(line)
                
                # Look for patterns that indicate questions
                elif any(keyword in line.lower() for keyword in ['question', 'what', 'how', 'why', 'when', 'where', '?']):
                    organized_content["sample_questions"].append(line)
                
                # Look for patterns that indicate answers
                elif any(keyword in line.lower() for keyword in ['answer', 'solution', 'approach', 'method', 'technique']):
                    organized_content["answers"].append(line)
                
                # Look for overview content
                elif any(keyword in line.lower() for keyword in ['overview', 'summary', 'introduction', 'background']):
                    organized_content["overview"][image_name] = line
        
        return organized_content
    
    def save_results(self, organized_content, output_file="meta_bible_extracted_content.md"):
        """Save the organized content to a markdown file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Meta Bible - Extracted Content\n\n")
            
            # Overview section
            if organized_content["overview"]:
                f.write("## Overview\n\n")
                for image_name, content in organized_content["overview"].items():
                    f.write(f"**{image_name}**: {content}\n\n")
            
            # Knowledge Points section
            if organized_content["knowledge_points"]:
                f.write("## Key Knowledge Points\n\n")
                for point in organized_content["knowledge_points"]:
                    f.write(f"- {point}\n")
                f.write("\n")
            
            # Sample Questions section
            if organized_content["sample_questions"]:
                f.write("## Sample Questions\n\n")
                for question in organized_content["sample_questions"]:
                    f.write(f"- {question}\n")
                f.write("\n")
            
            # Answers section
            if organized_content["answers"]:
                f.write("## Key Answers & Solutions\n\n")
                for answer in organized_content["answers"]:
                    f.write(f"- {answer}\n")
                f.write("\n")
            
            # Raw content section
            f.write("## Raw Extracted Content by Image\n\n")
            for image_name, content in organized_content["raw_content"].items():
                f.write(f"### {image_name}\n\n")
                f.write("```\n")
                f.write(content)
                f.write("\n```\n\n")
        
        print(f"Results saved to {output_file}")
    
    def save_json(self, organized_content, output_file="meta_bible_extracted_content.json"):
        """Save the organized content to a JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(organized_content, f, indent=2, ensure_ascii=False)
        
        print(f"JSON results saved to {output_file}")

def main():
    """Main function to run the extraction process."""
    print("Starting Meta Bible content extraction...")
    
    # Initialize the extractor
    extractor = MetaBibleExtractor()
    
    # Process all images
    extractor.process_all_images()
    
    if not extractor.extracted_content:
        print("No content was extracted from any images.")
        return
    
    # Organize the content
    print("\nOrganizing extracted content...")
    organized_content = extractor.organize_content()
    
    # Save results
    extractor.save_results(organized_content)
    extractor.save_json(organized_content)
    
    print("\nExtraction complete!")
    print(f"Processed {len(extractor.extracted_content)} images")
    print(f"Found {len(organized_content['knowledge_points'])} knowledge points")
    print(f"Found {len(organized_content['sample_questions'])} sample questions")
    print(f"Found {len(organized_content['answers'])} answers")

if __name__ == "__main__":
    main()

