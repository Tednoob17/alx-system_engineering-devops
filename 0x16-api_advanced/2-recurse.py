#!/usr/bin/python3
"""Return list of titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return list of titles of all hot articles for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        for child in data.get('children'):
            hot_list.append(child.get('data').get('title'))
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
