#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function to print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my_bot'}  # Custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children'][:10]  # Extract the first 10 posts
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)


if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name: ")
    top_ten(subreddit_name)
