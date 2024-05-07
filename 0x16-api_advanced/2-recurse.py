#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=None, after=None):
    
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        The list to store the titles of hot articles. Defaults to None.
        after (str, optional): The identifier of the last post in the current page. Defaults to None.
        
    Returns:
        list: A list containing the titles of all hot articles for the given subreddit. If no results are found, returns None.
    """

    if hot_list is None:
        hot_list = []

    # URL for the subreddit's hot posts
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': ''}  # Setting a custom User-Agent

    # Parameters for pagination
    params = {'limit': 100}  # Limit per request
    if after:
        params['after'] = after  # Add 'after' parameter if it exists

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params)

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts = data['data']['children']
        # Extract titles of posts and add to hot_list
        for post in posts:
            hot_list.append(post['data']['title'])
        # Check if there are more pages of results
        after = data['data']['after']
        if after:
            # Recursively call the function with the 'after' parameter to get the next page
            recurse(subreddit, hot_list, after)
        else:
            # Return the hot_list if no more pages are available
            return hot_list
    else:
        # If the subreddit is invalid or any other error occurs, return None
        return None

