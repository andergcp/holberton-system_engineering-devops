#!/usr/bin/python3
'''Reddit query'''
import requests


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    If an invalid subreddit is given return 0.
    '''

    b_url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'whatever'}
    response = requests.get(b_url, headers=headers)

    if response.status_code == 200:
        subs = response.json().get('data')
        subs = subs.get('subscribers')
        return subs
    else:
        return 0
