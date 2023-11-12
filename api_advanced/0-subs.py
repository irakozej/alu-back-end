#!/usr/bin/python3
"""
Module to query the Reddit API and get the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my_bot'}  # Custom User-Agent to avoid Too Many Requests error

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else:
        return 0


if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The number of subscribers for {subreddit_name} is: {subscribers}")
