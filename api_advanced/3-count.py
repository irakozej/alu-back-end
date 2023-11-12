#!/usr/bin/python3
"""
Module to define a recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function to count occurrences of keywords in the titles of hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count occurrences for.
        after (str): The 'after' parameter for pagination (default is None).
        counts (dict): Dictionary to store the counts of each keyword (default is None).

    Returns:
        None
    """
    if counts is None:
        counts = {}

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
            title = post['data']['title'].lower()  # Convert title to lowercase for case-insensitivity

            for word in word_list:
                word_lower = word.lower()

                # Check if the word is present in the title and not part of another word
                if f' {word_lower} ' in f' {title} ':
                    counts[word_lower] = counts.get(word_lower, 0) + 1

        after = data['data']['after']

        if after:
            # Recursive call with the 'after' parameter for pagination
            count_words(subreddit, word_list, after, counts)
        else:
            # Print the results in descending order by count, and alphabetically for ties
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                print(f'{word}: {count}')
    else:
        print(None)


if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name: ")
    keyword_list = input("Enter keywords (space-separated): ").split()

    count_words(subreddit_name, keyword_list)
