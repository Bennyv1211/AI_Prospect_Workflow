
# AI Prospect Workflow

## Overview
This Python script automates prospect company research for a sales team. It takes a company website URL as input and outputs a concise, informative article about the company.

## Features
- Scrapes content from the provided website
- Summarizes the extracted information into a readable article
- Uses OpenAI's GPT API for natural language processing

## Requirements
- Python 3.x
- Required Python Libraries: `requests`, `beautifulsoup4`, `openai`

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/your-username/AI_Prospect_Workflow.git
   cd AI_Prospect_Workflow
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Replace `your-openai-api-key` with your OpenAI API key in `main.py`.

## Usage
Run the script and provide a company website URL:
```
python main.py
```

## Output
The script generates a text file named `prospect_article.txt` containing the summarized article.
