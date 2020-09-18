#!/usr/bin/python3
'''Reddit query using recursion'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function returns None
    '''

    b_url = 'http://reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    headers = {'User-agent': 'whatever'}

    response = requests.get(b_url, headers=headers)
    if res.status_code == 200:
        top = response.json()
        key = top['data']['after']
        parent = top['data']['children']

        for obj in parent:
            hot_list.append(obj['data']['title'])

        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
