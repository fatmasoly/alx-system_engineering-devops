#!/usr/bin/python3
"""Module that queries the Reddit API and
    returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers={'User-agent': 'custom user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    return response.json().get('data', {}).get('subscribers', 0)
