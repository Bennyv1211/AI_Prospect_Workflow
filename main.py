
# AI Prospect Workflow
# A Python script to automate prospect research for a sales team

import requests
from bs4 import BeautifulSoup
import openai

# OpenAI API setup
openai.api_key = 'your-openai-api-key'

def fetch_website_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract text from specific sections (customize as needed)
    content = ''
    for section in soup.find_all(['h1', 'h2', 'p']):  # Add other tags if needed
        content += section.get_text(strip=True) + '\n'
    return content

def generate_summary(text):
    prompt = f"Summarize the following information into a concise, professional article suitable for a sales team:\n\n{text}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Input URL
    company_url = input("Enter the company website URL: ").strip()
    website_content = fetch_website_content(company_url)

    # Generate summary
    article = generate_summary(website_content)

    # Save to file
    output_file = "prospect_article.txt"
    with open(output_file, "w") as file:
        file.write(article)

    print(f"Prospect article generated and saved to {output_file}!")
