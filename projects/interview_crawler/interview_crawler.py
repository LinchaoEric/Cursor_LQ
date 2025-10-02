#!/usr/bin/env python3
"""
Product Data Scientist Interview Question Crawler
Crawls interview questions from 1point3acres forum
"""

import requests
from bs4 import BeautifulSoup
import time
import json
import re
from urllib.parse import urljoin, urlparse
import random

class InterviewCrawler:
    def __init__(self):
        self.base_url = "https://www.1point3acres.com/bbs/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        self.interview_questions = []
        
    def search_forum(self, keywords=None, max_pages=3):
        """
        Search for product data scientist related posts
        """
        if keywords is None:
            keywords = ['product data scientist', 'data scientist interview', 'product analytics', 'AB test', 'experiment']
        
        print(f"Searching for keywords: {keywords}")
        
        # Search in different forum sections
        search_urls = [
            "forum-237-1.html",  # Job hunting section
            "forum-238-1.html",  # Interview experience
            "forum-239-1.html",  # Career development
        ]
        
        for url_suffix in search_urls:
            try:
                url = urljoin(self.base_url, url_suffix)
                print(f"Crawling: {url}")
                
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                self.extract_threads(soup, keywords)
                
                # Be respectful with delays
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                print(f"Error crawling {url}: {e}")
                continue
    
    def extract_threads(self, soup, keywords):
        """
        Extract thread links that might contain interview questions
        """
        # Look for thread links
        thread_links = soup.find_all('a', href=re.compile(r'thread-\d+'))
        
        for link in thread_links[:10]:  # Limit to first 10 threads per page
            thread_title = link.get_text(strip=True)
            
            # Check if title contains relevant keywords
            if any(keyword.lower() in thread_title.lower() for keyword in keywords):
                thread_url = urljoin(self.base_url, link.get('href'))
                print(f"Found relevant thread: {thread_title}")
                self.extract_interview_question(thread_url, thread_title)
    
    def extract_interview_question(self, thread_url, thread_title):
        """
        Extract interview question from a specific thread
        """
        try:
            response = self.session.get(thread_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract post content
            posts = soup.find_all('div', class_=re.compile(r'post|message|content'))
            
            for post in posts[:3]:  # Look at first 3 posts
                content = post.get_text(strip=True)
                
                # Look for interview question patterns
                if self.is_interview_question(content):
                    question_data = {
                        'title': thread_title,
                        'url': thread_url,
                        'content': content[:500] + "..." if len(content) > 500 else content,
                        'keywords_found': self.extract_keywords(content),
                        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    self.interview_questions.append(question_data)
                    print(f"Extracted interview question: {thread_title[:50]}...")
                    break
            
            time.sleep(random.uniform(1, 2))
            
        except Exception as e:
            print(f"Error extracting from {thread_url}: {e}")
    
    def is_interview_question(self, content):
        """
        Determine if content contains interview question patterns
        """
        question_patterns = [
            r'interview.*question',
            r'asked.*during.*interview',
            r'product.*data.*scientist',
            r'AB.*test',
            r'experiment.*design',
            r'analytics.*challenge',
            r'case.*study',
            r'technical.*question',
            r'behavioral.*question'
        ]
        
        content_lower = content.lower()
        return any(re.search(pattern, content_lower) for pattern in question_patterns)
    
    def extract_keywords(self, content):
        """
        Extract relevant keywords from content
        """
        keywords = []
        keyword_patterns = [
            'product analytics', 'AB testing', 'experiment', 'data analysis',
            'SQL', 'Python', 'statistics', 'machine learning', 'metrics',
            'conversion rate', 'user behavior', 'funnel analysis', 'cohort analysis'
        ]
        
        content_lower = content.lower()
        for keyword in keyword_patterns:
            if keyword.lower() in content_lower:
                keywords.append(keyword)
        
        return keywords
    
    def save_results(self, filename='interview_questions.json'):
        """
        Save extracted questions to JSON file
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.interview_questions, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(self.interview_questions)} interview questions to {filename}")
    
    def print_summary(self):
        """
        Print a summary of extracted questions
        """
        print(f"\n=== CRAWLING SUMMARY ===")
        print(f"Total questions extracted: {len(self.interview_questions)}")
        
        if self.interview_questions:
            print(f"\nSample questions:")
            for i, question in enumerate(self.interview_questions[:3], 1):
                print(f"\n{i}. {question['title']}")
                print(f"   Keywords: {', '.join(question['keywords_found'])}")
                print(f"   URL: {question['url']}")

def main():
    """
    Main function to run the crawler
    """
    print("Starting Product Data Scientist Interview Question Crawler...")
    print("Target website: https://www.1point3acres.com/bbs/")
    
    crawler = InterviewCrawler()
    
    # Custom keywords for product data scientist interviews
    keywords = [
        'product data scientist',
        'data scientist interview',
        'product analytics',
        'AB test',
        'experiment design',
        'analytics case study',
        'product metrics',
        'user behavior analysis',
        'conversion optimization'
    ]
    
    try:
        crawler.search_forum(keywords=keywords, max_pages=2)
        crawler.save_results()
        crawler.print_summary()
        
    except KeyboardInterrupt:
        print("\nCrawling interrupted by user")
        crawler.save_results()
    except Exception as e:
        print(f"Error during crawling: {e}")
        crawler.save_results()

if __name__ == "__main__":
    main()
