# Cursor_LQ - Interview Preparation & Data Science Projects

my cursor playground

This repository contains various projects and resources for interview preparation, data science tools, and audio processing utilities.

## 📁 Project Structure

### 🎯 Interview Preparation
- **`Meta Interview/`** - Meta interview preparation materials
  - Technical skills, analytics execution, analytical reasoning guides
  - Behavioral interview preparation
  - SQL whiteboard exercises

### 🗂️ Projects

#### 📊 AB Testing
- **`projects/ab_testing/`** - AB testing interview resources
  - Interview guides and notes
  - Webinar recordings
  - Transcription tools

#### 🎵 Audio Processing
- **`projects/audio_processing/`** - Audio transcription and analysis tools
  - Whisper transcription scripts
  - Interview audio analysis (Cedar, DoorDash)
  - Audio requirements and dependencies

#### 🕷️ Interview Crawler
- **`projects/interview_crawler/`** - Web scraping tools for interview questions
  - Forum crawler for interview questions
  - Improved crawler with enhanced features
  - Extracted interview questions database

#### 📚 Meta Bible Extractor
- **`projects/meta_bible_extractor/`** - Meta interview content extraction tools
  - Multiple extractor scripts (simple, enhanced, statistics)
  - Comprehensive guides and organized content
  - Statistics extraction summaries

### 📖 Documentation
- **`docs/`** - Project documentation and requirements
  - Main README and requirements files
  - Installation and usage instructions

### 🖼️ Resources
- **`meta_bible/`** - Meta interview image resources
  - Interview preparation images and screenshots

## 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r docs/requirements.txt
   ```

2. **Run Specific Projects**
   - **Interview Crawler**: `python projects/interview_crawler/interview_crawler.py`
   - **Audio Transcription**: `python projects/audio_processing/whisper_transcriber.py`
   - **Meta Bible Extraction**: `python projects/meta_bible_extractor/meta_bible_extractor.py`

## 📋 Project Descriptions

### Interview Crawler
Web scraping tool that extracts product data scientist interview questions from forums. Features keyword filtering, respectful crawling with delays, and JSON output.

### Audio Processing
Collection of audio transcription tools using Whisper AI, with specific implementations for interview analysis and feedback generation.

### Meta Bible Extractor
Tools for extracting and organizing Meta interview content, including statistics guides and comprehensive preparation materials.

### AB Testing Resources
Interview preparation materials specifically focused on AB testing concepts, including guides, notes, and webinar recordings.

## 🛠️ Technologies Used

- **Python** - Main programming language
- **BeautifulSoup** - Web scraping
- **Whisper AI** - Audio transcription
- **SQLite** - Database operations
- **JSON** - Data storage and exchange

## 📝 Notes

- All projects include their own requirements files
- Audio files are stored in respective project directories
- Interview materials are organized by company and topic
- Extraction tools support multiple output formats (JSON, Markdown)

## 🔧 Maintenance

This repository is organized for easy navigation and maintenance:
- Related files are grouped in project folders
- Documentation is centralized in the `docs/` folder
- Each project has its own dependencies and requirements
- Clear separation between interview prep materials and tools

