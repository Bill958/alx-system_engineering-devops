#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords.
    
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str, optional): The identifier of the last post in the current page. Defaults to None.
        counts (dict, optional): A dictionary to store the counts of keywords. Defaults to None.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}  

    
    params = {'limit': 100}  
    if after:
        params['after'] = after 

    
    response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            title = post['data']['title'].lower()  
            
            for word in word_list:
                if word.lower() in title.split():
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1
        
        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))  
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Error:", response.status_code)

