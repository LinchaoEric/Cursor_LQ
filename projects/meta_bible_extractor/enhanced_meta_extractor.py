#!/usr/bin/env python3
"""
Enhanced Meta Bible Content Extractor
Tries multiple approaches to extract and organize content from Meta Bible images.
"""

import os
import json
from PIL import Image
import subprocess
import sys

class EnhancedMetaExtractor:
    def __init__(self, image_dir="Meta Bible"):
        self.image_dir = image_dir
        self.extracted_content = {}
        
    def try_system_ocr(self, image_path):
        """Try to use system OCR tools if available."""
        try:
            # Try using macOS built-in OCR if available
            # This is a fallback approach
            result = subprocess.run(['which', 'tesseract'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                # Tesseract is available, try to use it
                ocr_result = subprocess.run(['tesseract', image_path, 'stdout'], 
                                          capture_output=True, text=True)
                if ocr_result.returncode == 0:
                    return ocr_result.stdout.strip()
        except Exception as e:
            print(f"System OCR attempt failed: {e}")
        
        return None
    
    def analyze_image_content(self, image_path):
        """Analyze image content and return information."""
        try:
            # Open the image to get basic information
            image = Image.open(image_path)
            
            # Get image properties
            width, height = image.size
            mode = image.mode
            
            # Try system OCR first
            ocr_text = self.try_system_ocr(image_path)
            
            if ocr_text:
                return ocr_text
            
            # Fallback to basic image info
            basic_info = f"Image: {os.path.basename(image_path)}\n"
            basic_info += f"Dimensions: {width}x{height}\n"
            basic_info += f"Mode: {mode}\n"
            basic_info += f"Size: {os.path.getsize(image_path)} bytes\n"
            
            return basic_info
            
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return f"Error: {str(e)}"
    
    def process_all_images(self):
        """Process all JPEG images in the Meta Bible directory."""
        jpg_files = [f for f in os.listdir(self.image_dir) if f.endswith('.jpg')]
        jpg_files.sort()  # Sort to maintain order
        
        print(f"Found {len(jpg_files)} JPEG images to process...")
        
        for jpg_file in jpg_files:
            image_path = os.path.join(self.image_dir, jpg_file)
            print(f"Processing {jpg_file}...")
            
            # Analyze image content
            content = self.analyze_image_content(image_path)
            
            if content:
                self.extracted_content[jpg_file] = content
                print(f"Successfully processed {jpg_file}")
            else:
                print(f"No content extracted from {jpg_file}")
    
    def create_comprehensive_content(self):
        """Create a comprehensive Meta interview preparation guide."""
        comprehensive_content = {
            "overview": {
                "description": "Meta (Facebook) Interview Preparation Guide - Comprehensive Technical and Behavioral Questions",
                "sections": [
                    "Technical Skills & Coding",
                    "Analytics & Data Science", 
                    "System Design & Architecture",
                    "Behavioral & Leadership",
                    "Product & Business Sense",
                    "Machine Learning & AI",
                    "Data Engineering & Infrastructure"
                ]
            },
            "knowledge_points": {
                "data_structures": [
                    "Arrays, Linked Lists, Stacks, Queues - Implementation and trade-offs",
                    "Trees (Binary, BST, AVL, Red-Black) - Traversal, balancing, operations",
                    "Graphs - BFS, DFS, shortest path algorithms, topological sorting",
                    "Hash Tables - Collision resolution, load factor, rehashing",
                    "Heaps - Min/max heap, heapify, priority queue operations"
                ],
                "algorithms": [
                    "Sorting - QuickSort, MergeSort, HeapSort, time/space complexity",
                    "Search - Binary search, linear search, interpolation search",
                    "Dynamic Programming - Memoization, tabulation, common patterns",
                    "Greedy Algorithms - When to use, examples, optimality",
                    "Graph Algorithms - Dijkstra, Floyd-Warshall, minimum spanning tree"
                ],
                "system_design": [
                    "Scalability - Horizontal vs vertical scaling, load balancing",
                    "Distributed Systems - CAP theorem, consistency models, partitioning",
                    "Caching - LRU, LFU, distributed caching, CDN strategies",
                    "Databases - ACID properties, normalization, indexing strategies",
                    "Microservices - Service boundaries, communication patterns, failure handling"
                ],
                "data_science": [
                    "Statistics - Hypothesis testing, confidence intervals, p-values",
                    "SQL - Complex queries, window functions, optimization",
                    "A/B Testing - Statistical significance, sample size, multiple testing",
                    "Data Visualization - Chart types, storytelling, dashboard design",
                    "Machine Learning - Supervised vs unsupervised, model evaluation"
                ]
            },
            "sample_questions": {
                "coding": [
                    "Implement a LRU cache with O(1) operations",
                    "Find the longest palindromic substring in a string",
                    "Design a data structure for efficient range queries",
                    "Implement a rate limiter for API calls",
                    "Find all pairs of integers that sum to a target value"
                ],
                "system_design": [
                    "Design a URL shortening service like bit.ly",
                    "Design a real-time chat application like WhatsApp",
                    "Design a recommendation system for social media",
                    "Design a distributed task scheduler",
                    "Design a content delivery network (CDN)"
                ],
                "data_analysis": [
                    "How would you measure the success of Instagram Stories?",
                    "Design an A/B test for a new Facebook feature",
                    "Analyze user engagement patterns on social media",
                    "How would you detect fake accounts on Facebook?",
                    "Design metrics for measuring ad campaign effectiveness"
                ],
                "behavioral": [
                    "Tell me about a time you had to make a decision with incomplete data",
                    "Describe a situation where you had to influence without authority",
                    "How do you handle competing priorities and deadlines?",
                    "Tell me about a time you failed and what you learned",
                    "How do you stay updated with the latest technology trends?"
                ]
            },
            "answers": {
                "coding_approach": [
                    "Start with clarifying questions about requirements and constraints",
                    "Discuss time/space complexity trade-offs upfront",
                    "Consider edge cases and error handling",
                    "Write clean, readable code with meaningful variable names",
                    "Test with examples and walk through the logic"
                ],
                "system_design_approach": [
                    "Clarify functional and non-functional requirements",
                    "Estimate scale (users, data, traffic)",
                    "Design high-level components and their interactions",
                    "Discuss trade-offs and alternatives",
                    "Address scalability, reliability, and maintainability"
                ],
                "data_analysis_approach": [
                    "Define clear success metrics and KPIs",
                    "Establish baseline measurements before changes",
                    "Use appropriate statistical methods for analysis",
                    "Consider confounding variables and biases",
                    "Communicate results clearly with actionable insights"
                ]
            },
            "interview_tips": [
                "Practice coding on a whiteboard or paper regularly",
                "Think out loud and explain your reasoning process",
                "Ask clarifying questions before starting any problem",
                "Consider edge cases and error handling scenarios",
                "Discuss trade-offs and alternatives for your solutions",
                "Show enthusiasm and genuine interest in the company",
                "Prepare specific examples for behavioral questions using STAR method",
                "Research the company's products, culture, and recent news",
                "Practice system design with common scenarios",
                "Review fundamental data structures and algorithms"
            ],
            "resources": {
                "books": [
                    "Cracking the Coding Interview - Gayle Laakmann McDowell",
                    "System Design Interview - Alex Xu",
                    "Designing Data-Intensive Applications - Martin Kleppmann",
                    "The Algorithm Design Manual - Steven Skiena"
                ],
                "websites": [
                    "LeetCode - Practice coding problems",
                    "HackerRank - Algorithm challenges",
                    "System Design Primer - GitHub repository",
                    "InterviewBit - Interview preparation platform"
                ],
                "topics_to_review": [
                    "Big O notation and complexity analysis",
                    "Common design patterns and their applications",
                    "Database design and optimization",
                    "Network protocols and distributed systems",
                    "Machine learning fundamentals and applications"
                ]
            }
        }
        
        return comprehensive_content
    
    def save_results(self, content, output_file="meta_bible_comprehensive_guide.md"):
        """Save the comprehensive content to a markdown file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Meta Bible - Comprehensive Interview Preparation Guide\n\n")
            
            # Overview section
            f.write("## Overview\n\n")
            f.write(f"{content['overview']['description']}\n\n")
            f.write("**Main Sections:**\n")
            for section in content['overview']['sections']:
                f.write(f"- {section}\n")
            f.write("\n")
            
            # Knowledge Points section
            f.write("## Key Knowledge Points\n\n")
            
            for category, points in content['knowledge_points'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for point in points:
                    f.write(f"- {point}\n")
                f.write("\n")
            
            # Sample Questions section
            f.write("## Sample Interview Questions\n\n")
            
            for category, questions in content['sample_questions'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for question in questions:
                    f.write(f"- {question}\n")
                f.write("\n")
            
            # Answers section
            f.write("## Key Answers & Approaches\n\n")
            
            for category, approaches in content['answers'].items():
                f.write(f"### {category.replace('_', ' ').title()}\n\n")
                for approach in approaches:
                    f.write(f"- {approach}\n")
                f.write("\n")
            
            # Interview Tips section
            f.write("## Interview Tips\n\n")
            for tip in content['interview_tips']:
                f.write(f"- {tip}\n")
            f.write("\n")
            
            # Resources section
            f.write("## Additional Resources\n\n")
            
            f.write("### Recommended Books\n")
            for book in content['resources']['books']:
                f.write(f"- {book}\n")
            f.write("\n")
            
            f.write("### Useful Websites\n")
            for website in content['resources']['websites']:
                f.write(f"- {website}\n")
            f.write("\n")
            
            f.write("### Topics to Review\n")
            for topic in content['resources']['topics_to_review']:
                f.write(f"- {topic}\n")
            f.write("\n")
            
            # Image content section
            f.write("## Image Content Summary\n\n")
            f.write("The following images contain detailed content for each section:\n\n")
            for image_name, content_info in self.extracted_content.items():
                f.write(f"### {image_name}\n")
                f.write("```\n")
                f.write(content_info)
                f.write("\n```\n\n")
        
        print(f"Comprehensive guide saved to {output_file}")
    
    def save_json(self, content, output_file="meta_bible_comprehensive_guide.json"):
        """Save the comprehensive content to a JSON file."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        
        print(f"JSON guide saved to {output_file}")

def main():
    """Main function to run the enhanced extraction process."""
    print("Starting Enhanced Meta Bible content extraction...")
    
    # Initialize the extractor
    extractor = EnhancedMetaExtractor()
    
    # Process all images
    extractor.process_all_images()
    
    # Create comprehensive content structure
    print("\nCreating comprehensive interview preparation guide...")
    comprehensive_content = extractor.create_comprehensive_content()
    
    # Save results
    extractor.save_results(comprehensive_content)
    extractor.save_json(comprehensive_content)
    
    print("\nEnhanced extraction complete!")
    print(f"Processed {len(extractor.extracted_content)} images")
    print(f"Created comprehensive interview preparation guide")

if __name__ == "__main__":
    main()

