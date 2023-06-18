#!/usr/bin/python3
"""Return top ten posts from subreddit"""

import requests


def top_ten(subreddit):
    """Return top ten posts from subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("None")
        return
    data = response.json()
    for post in data["data"]["children"]:
        print(post["data"]["title"])
