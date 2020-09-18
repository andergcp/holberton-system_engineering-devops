#!/usr/bin/python3
'''Reddit query'''
import requests


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, prints None.
    '''

    b_url = 'http://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'whatever'}

    response = requests.get(b_url, headers=headers)
    if response.status_code == 200:
        top = response.json()
        for i in range(10):
            print(top['data']['children'][i]['data']['title'])
    else:
        return print('None')
