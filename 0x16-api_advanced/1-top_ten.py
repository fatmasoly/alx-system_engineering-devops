#!/usr/bin/python3
"""Reddit API Module"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API to fetch the titles of the
        first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            print("No posts found in the subreddit.")
            return
        print("Top 10 hot posts in r/{}:".format(subreddit))
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
