#!/usr/bin/python3
'''Reddit query using recursion'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function returns None
    '''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'Python3/requests_library/1'}
    redirects = False
    if len(hot_list) == 0:
        request_subreddit = requests.get(url, headers=headers,
                                         allow_redirects=redirects)
    else:
        data = {'after': after}
        request_subreddit = requests.get(url, headers=headers, params=data,
                                         allow_redirects=redirects)
    if request_subreddit.status_code == 200:
        subreddit_json = request_subreddit.json()
        for children in subreddit_json['data']['children']:
            hot_list.append(children)
        end_value = subreddit_json['data']['after']
        if end_value is None:
            return hot_list
        return recurse(subreddit, hot_list, end_value)
    return None
