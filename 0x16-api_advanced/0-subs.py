#!/usr/bin/python3
"""function that queries the Reddit API and returns the
number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = 'https://www.reddit.com/dev/api/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Pyr6l05mpGIDtYy5bLjIgw'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
