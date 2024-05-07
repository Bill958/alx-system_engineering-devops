#!/usr/bin/python3
"""
0-subs
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
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Chrome/billreddit'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Checking if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # return number of subscribers
        return data['data']['subscribers']
    else:
        # If the subreddit is invalid or any other error occurs, return 0
        print("Error:", response.status_code)
        return 0

# Testing the function
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

