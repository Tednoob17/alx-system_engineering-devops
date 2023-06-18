#!/usr/bin/python3
"""Return list of titles of all hot articles for a given subreddit"""
import requests


def count_words(subreddit, word_list, r_list=[], after=None):
    """Return list of titles of all hot articles for a given subreddit

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        r_list (dict): The dictionary of words and counts.
        after (str): The parameter for the next page of the API results.
    """

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    response = requests.get(url, headers={'User-Agent': 'test'})

    if after is None:
        word_list = [word.lower() for word in word_list]
    try:
        response.raise_for_status()
    except:
        print("")
        return None

    if response.status_code == 200:
        response = response.json()['data']
        aft = response['after']
        response = response['children']
        for post in response:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    r_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, r_list, aft)
        else:
            res = {}
            for word in r_list:
                if word.lower() in res.keys():
                    res[word.lower()] += 1
                else:
                    res[word.lower()] = 1
            for key, value in sorted(res.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
