#!/usr/bin/python3
"""A script that queries reddit Api"""

import requests


def number_of_subscribers(subreddit):
    """A function that returns the number of subscribers."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    custom_header = {'User-Agent': 'myreddit_script'}
    response = requests.get(url, allow_redirects=False, headers=custom_header)
    if response.status_code == 404:
        return 0
    elif response.status_code == 200:
        result = response.json()
        data = result.get('data')
        count = data.get('subscribers')
        if count is None:
            return 0
        return count
