#!/usr/bin/python3
"""
Queries the Reddit API to retrieve the number of subscribers for a given subreddit.
"""

import requests

def
 
number_of_subscribers(subreddit):

    
"""
    Queries the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit, or 0 if not found or invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my_reddit_app'}  # Set a custom User-Agent

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent redirects
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        return data['data']['subscribers']

    except requests.exceptions.RequestException:
        return 0  # Handle errors (e.g., invalid subreddit, network issues)
