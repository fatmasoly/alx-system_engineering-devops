#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'alxAPI'}
    res = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=headers,
        allow_redirects=False
    )

    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
