#!/usr/bin/env python3
"""
Site-Sentinel: Website Monitoring & Latency Tracker
Demonstrates: API usage, Error Handling, and Logging.
"""

import requests
import time
from datetime import datetime

# A list of websites to monitor
SITES = ["https://www.google.com", "https://www.github.com", "https://www.upwork.com"]

def check_health():
    print(f"--- Monitoring Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    for url in SITES:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            latency = round((time.time() - start_time) * 1000, 2)
            
            if response.status_code == 200:
                print(f"[ONLINE] {url:25} | Latency: {latency: >7} ms")
            else:
                print(f"[ALARM]  {url:25} | Status: {response.status_code}")
        except Exception as e:
            print(f"[FAILED] {url:25} | Error: {str(e)}")

if __name__ == "__main__":
    check_health()
