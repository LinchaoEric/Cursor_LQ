# Product Data Scientist Interview Question Crawler

This Python script crawls the 1point3acres forum to extract product data scientist interview questions.

## Features

- Crawls multiple forum sections for relevant interview questions
- Filters content based on product data scientist keywords
- Extracts interview questions with metadata (title, URL, content, keywords)
- Saves results to JSON format
- Implements respectful crawling with delays
- Handles errors gracefully

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python interview_crawler.py
```

The script will:
1. Search for threads containing product data scientist interview questions
2. Extract relevant content from matching threads
3. Save the results to `interview_questions.json`
4. Display a summary of extracted questions

## Output

The script generates a JSON file (`interview_questions.json`) with the following structure:

```json
[
  {
    "title": "Thread title",
    "url": "Thread URL",
    "content": "Extracted content (truncated to 500 chars)",
    "keywords_found": ["keyword1", "keyword2"],
    "timestamp": "2024-01-01 12:00:00"
  }
]
```

## Customization

You can modify the keywords in the `main()` function to search for different types of interview questions:

```python
keywords = [
    'product data scientist',
    'data scientist interview',
    'product analytics',
    'AB test',
    'experiment design',
    # Add your own keywords here
]
```

## Notes

- The script implements respectful crawling with random delays
- It searches in job hunting, interview experience, and career development sections
- Content is filtered using regex patterns to identify interview questions
- The script handles network errors and continues crawling other pages

## Disclaimer

Please respect the website's robots.txt and terms of service. This script is for educational purposes only. Consider implementing proper rate limiting for production use.

