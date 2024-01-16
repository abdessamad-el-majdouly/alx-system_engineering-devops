#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"  # Fix the URL
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/dblay112_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
