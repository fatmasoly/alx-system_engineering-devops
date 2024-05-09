#!/usr/bin/python3
""" Module that queries the Reddit API and
returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    x = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    if x.status_code == 200:
        try:
            return x.json()['data']['subscribers']
        except:
            return 0
    else:
        return 0
