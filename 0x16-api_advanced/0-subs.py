#!/usr/bin/python3
"""Module that queries the Reddit API and
    returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if subreddit is None:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
