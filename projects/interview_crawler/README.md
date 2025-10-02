# Interview Crawler Project

This project contains web scraping tools for extracting interview questions from forums.

## Files

- `interview_crawler.py` - Main crawler script
- `improved_crawler.py` - Enhanced version with additional features
- `interview_questions.json` - Extracted interview questions database

## Usage

```bash
python interview_crawler.py
```

## Features

- Crawls multiple forum sections for relevant interview questions
- Filters content based on product data scientist keywords
- Extracts interview questions with metadata
- Saves results to JSON format
- Implements respectful crawling with delays
- Handles errors gracefully

## Output

Generates a JSON file with interview questions including:
- Thread title and URL
- Extracted content
- Keywords found
- Timestamp


