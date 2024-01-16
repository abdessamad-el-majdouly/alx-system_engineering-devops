#!/usr/bin/python3
"""function that prints the title of forst 10 hot posts"""

import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    header = {'User-agent': 'Chrome'}
    try:
        response = requests.get(url, headers=header, params=params)
        response.raise_for_status()

        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print("None")
        else:
            for post in posts:
                title = post["data"]["title"]
                print(title)

    except requests.exceptions.RequestException:
        print("None")
