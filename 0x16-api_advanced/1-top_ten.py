#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "AdvancedAPI/1.0/bill958"
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response
    data = response.json()

    # Extract and print titles of the first 10 posts
    for post in data['data']['children'][:10]:
        print(post['data']['title'])

