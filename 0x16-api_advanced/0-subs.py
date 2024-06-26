#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers of the subreddit. If the subreddit is invalid or an error occurs, returns 0.
    """
    # URL for the subreddit's information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Chrome/billreddit'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Checking if the response is successful
    if response.status_code == 200:
        # return number of subscribers
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        # If the subreddit is invalid or any other error occurs, return 0
        return 0

