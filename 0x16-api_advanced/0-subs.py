#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'CustomUserAgent/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']

        elif response.status_code == 404:
            return 0

        else:
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
