#!/usr/bin/python3
"""
Module to define a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to get the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles (default is an empty list).
        after (str): The 'after' parameter for pagination (default is None).

    Returns:
        list: List containing the titles of all hot articles, or None if no results are found.
    """
    if not after:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'my_bot'}  # Custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']

        if after:
            # Recursive call with the 'after' parameter for pagination
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name: ")
    result = recurse(subreddit_name)

    if result is not None:
        for title in result:
            print(title)
    else:
        print(None)
