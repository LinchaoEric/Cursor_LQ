#!/usr/bin/env python3
"""
Improved Product Data Scientist Interview Question Crawler
Crawls interview questions from 1point3acres forum with better error handling
"""

import requests
from bs4 import BeautifulSoup
import time
import json
import re
from urllib.parse import urljoin, urlparse
import random

class ImprovedInterviewCrawler:
    def __init__(self):
        self.base_url = "https://www.1point3acres.com/bbs/"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        })
        self.interview_questions = []
        
    def test_connection(self):
        """
        Test if we can access the website
        """
        try:
            print("Testing connection to 1point3acres...")
            response = self.session.get(self.base_url, timeout=10)
            response.raise_for_status()
            print(f"Connection successful! Status code: {response.status_code}")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
    
    def explore_site_structure(self):
        """
        Explore the site structure to find relevant sections
        """
        try:
            response = self.session.get(self.base_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            print("Exploring site structure...")
            
            # Look for navigation links
            nav_links = soup.find_all('a', href=True)
            relevant_sections = []
            
            for link in nav_links:
                href = link.get('href', '')
                text = link.get_text(strip=True)
                
                # Look for job-related sections
                if any(keyword in text.lower() for keyword in ['job', 'interview', 'career', 'work', 'employment']):
                    relevant_sections.append({
                        'text': text,
                        'href': href,
                        'url': urljoin(self.base_url, href)
                    })
            
            print(f"Found {len(relevant_sections)} potentially relevant sections:")
            for section in relevant_sections[:5]:  # Show first 5
                print(f"  - {section['text']}: {section['url']}")
            
            return relevant_sections
            
        except Exception as e:
            print(f"Error exploring site structure: {e}")
            return []
    
    def search_with_keywords(self, keywords=None):
        """
        Search for content using keywords
        """
        if keywords is None:
            keywords = ['product data scientist', 'data scientist interview', 'product analytics', 'AB test']
        
        print(f"Searching with keywords: {keywords}")
        
        # Try different search approaches
        search_urls = [
            f"{self.base_url}search.php?mod=forum&searchid=1&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw={'+'.join(keywords[:2])}",
            f"{self.base_url}forum.php?mod=forumdisplay&fid=237",  # Job hunting
            f"{self.base_url}forum.php?mod=forumdisplay&fid=238",  # Interview experience
        ]
        
        for search_url in search_urls:
            try:
                print(f"Trying search URL: {search_url}")
                response = self.session.get(search_url, timeout=15)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                self.extract_from_page(soup, search_url)
                
                time.sleep(random.uniform(2, 4))
                
            except Exception as e:
                print(f"Error with search URL {search_url}: {e}")
                continue
    
    def extract_from_page(self, soup, page_url):
        """
        Extract content from a page
        """
        # Look for different types of links that might contain interview questions
        link_patterns = [
            r'thread-\d+',
            r'forum\.php\?mod=viewthread',
            r'viewthread\.php',
        ]
        
        all_links = soup.find_all('a', href=True)
        relevant_links = []
        
        for link in all_links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # Check if link matches patterns and has relevant text
            if any(re.search(pattern, href) for pattern in link_patterns):
                if len(text) > 10 and any(keyword in text.lower() for keyword in ['interview', 'data', 'product', 'analytics', 'scientist']):
                    relevant_links.append({
                        'text': text,
                        'href': href,
                        'url': urljoin(page_url, href)
                    })
        
        print(f"Found {len(relevant_links)} potentially relevant links")
        
        # Process first few links
        for link_info in relevant_links[:5]:
            self.process_thread(link_info)
    
    def process_thread(self, link_info):
        """
        Process a single thread
        """
        try:
            print(f"Processing thread: {link_info['text'][:50]}...")
            
            response = self.session.get(link_info['url'], timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract content from different possible selectors
            content_selectors = [
                '.t_f', '.postcontent', '.message', '.content', '.post',
                'div[class*="post"]', 'div[class*="message"]', 'div[class*="content"]'
            ]
            
            content = ""
            for selector in content_selectors:
                elements = soup.select(selector)
                if elements:
                    content = ' '.join([elem.get_text(strip=True) for elem in elements[:3]])
                    break
            
            if content and self.is_interview_question(content):
                question_data = {
                    'title': link_info['text'],
                    'url': link_info['url'],
                    'content': content[:800] + "..." if len(content) > 800 else content,
                    'keywords_found': self.extract_keywords(content),
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                }
                
                self.interview_questions.append(question_data)
                print(f"✓ Extracted interview question: {link_info['text'][:50]}...")
            
            time.sleep(random.uniform(1, 3))
            
        except Exception as e:
            print(f"Error processing thread {link_info['url']}: {e}")
    
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
            r'behavioral.*question',
            r'data.*analysis',
            r'SQL.*question',
            r'Python.*question',
            r'statistics.*question'
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
            'conversion rate', 'user behavior', 'funnel analysis', 'cohort analysis',
            'interview', 'data scientist', 'product', 'analytics'
        ]
        
        content_lower = content.lower()
        for keyword in keyword_patterns:
            if keyword.lower() in content_lower:
                keywords.append(keyword)
        
        return list(set(keywords))  # Remove duplicates
    
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
                print(f"   Content preview: {question['content'][:100]}...")
        else:
            print("No interview questions found. This could be due to:")
            print("- Website structure changes")
            print("- Access restrictions")
            print("- No relevant content found")
            print("- Network connectivity issues")

def main():
    """
    Main function to run the improved crawler
    """
    print("Starting Improved Product Data Scientist Interview Question Crawler...")
    print("Target website: https://www.1point3acres.com/bbs/")
    
    crawler = ImprovedInterviewCrawler()
    
    # Test connection first
    if not crawler.test_connection():
        print("Cannot connect to the website. Please check your internet connection.")
        return
    
    # Explore site structure
    sections = crawler.explore_site_structure()
    
    # Search with keywords
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
        crawler.search_with_keywords(keywords)
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
