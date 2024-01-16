#!/usr/bin/python3
"""A script that queries reddit Api"""

import requests


def top_ten(subreddit):
    """Prints the top ten hot post in a subreddit."""
    header = {'User-Agent': '1-top_ten.py'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(
            url, params={'limit': 10}, headers=header, allow_redirects=False
            )
    if response.status_code == 404:
        print(None)
    else:
        result = response.json().get('data')
        result = result.get('children')
        for data in result:
            print(data.get('data', {}).get('title', None))
