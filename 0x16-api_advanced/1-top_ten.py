#!/usr/bin/python3
"""Contains top_ten function"""
import requests
import sys

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return
        response_text = response.text
        if not response_text:
            print("Empty response")
            return
        results = response.json().get("data", {})
        for child in results.get("children", []):
            title = child.get("data", {}).get("title")
            if title:
                print(title)
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except ValueError as e:
        print(f"JSON decoding failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        top_ten(sys.argv[1])
    else:
        print("Usage: ./1-main.py <subreddit>")
