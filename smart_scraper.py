#!/usr/bin/env python3
"""
Smart-Scraper: Dynamic News Headline Extractor
Demonstrates: Web Scraping, HTML Parsing, and Data Extraction.
"""

import requests
from bs4 import BeautifulSoup

def get_headlines():
    url = "https://news.ycombinator.com/" # Hacker News
    print(f"Scraping latest tech trends from {url}...")
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = soup.find_all('span', class_='titleline')
        
        print("\n--- Current Top Tech Headlines ---")
        for i, story in enumerate(stories[:10], 1):
            title = story.find('a').text
            link = story.find('a')['href']
            print(f"{i}. {title}")
            print(f"   Link: {link}\n")
            
    except Exception as e:
        print(f"Scrape failed: {e}")

if __name__ == "__main__":
    get_headlines()
