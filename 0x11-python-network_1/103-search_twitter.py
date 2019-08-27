#!/usr/bin/python3
"""Module to perform a Twitter search"""


import base64
import requests
import sys


if __name__ == '__main__':
    consumer = base64.b64encode((sys.argv[1] + ':' + sys.argv[1]).encode())
    response = requests.post(
        'https://api.twitter.com/oauth2/token',
        headers={
            'Authorization': 'Basic ' + consumer.decode(),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        data={'grant_type': 'client_credentials'}
    )
    token = response.json().get('access_token')
    response = requests.get(
        'https://api.twitter.com/1.1/search/tweets.json',
        headers={'Authorization': 'Bearer ' + token},
        params={'q': sys.argv[3], 'count': '5'}
    )
    tweets = response.json().get('statuses')
    for tweet in tweets:
        print('[{}] {} by {}'.format(
            tweet.get('id'),
            tweet.get('text'),
            tweet.get('user').get('name')
        ))
