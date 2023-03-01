#!/usr/bin/python3
"""Description of module"""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{sub}/hot/.json".format(sub=subreddit)
    headers = {
        'User-Agent': 'ALX API Fetcher',
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    info = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if info.status_code == 200:
        data = info.json().get("data")
        after = data.get("after")
        count = data.get("dist")
        for i in data.get("children"):
            hot_list.append(i.get("data").get("title"))
        if after is not None:
            return recurse(
                subreddit, hot_list=hot_list, after=after, count=count)
        return hot_list
    else:
        return None
