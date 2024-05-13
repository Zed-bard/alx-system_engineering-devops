#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.ok:
            results = response.json().get("data", {})
            for child in results.get("children", []):
                title = child.get("data", {}).get("title")
                if title:
                    print(title)
        else:
            print("None")
    except requests.RequestException as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"JSON decoding failed: {e}")


if __name__ == "__main__":
    top_ten("python")
