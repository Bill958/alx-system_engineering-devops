#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    """
    # URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'AdvancedAPI/1.0/bill958'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers,allow_redirects=False)

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and print titles of the first 10 posts
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        # If the subreddit is invalid or any other error occurs, print None
        print(None)

