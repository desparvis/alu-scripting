#!/usr/bin/python3
"""DOCUMENTING"""
import requests

def top_ten(subreddit):
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        for post in data.get('children', [])[:10]:
            print(post['data']['title'])
        return "OK"
    return None
