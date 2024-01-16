#!/usr/bin/python3
"""function that queries the reddit API"""

import requests


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    header = {'User-Agent': 'Get subscribers info'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    data = requests.get(url, headers=header, allow_redirects=False)

    if data.status_code == 200:
        try:
            data = data.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0
