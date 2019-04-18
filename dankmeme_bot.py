#!/usr/bin/python

import praw
import urllib.request
import os
import time
import datetime

# Path to save images to. 
PATH = "E:\\Media\\Pictures\\Memes\\Dankmemes"

# Get bot data and subreddit instance. 
reddit = praw.Reddit('BOT')
subreddit = reddit.subreddit('dankmemes')

print("")
print("Bot running. Parsing posts...")
print("")
for submission in subreddit.hot(limit=5):
    valid_types = (".jpg", ".png")
    url_string = str(submission.url)
    
    if url_string.endswith(valid_types):
        # Get file type. 
        file_type = url_string[-4:]

        # Print title and url of submission in console. 
        print("Title: " + submission.title)
        print("URL  : " + submission.url)
        print("-------------------------------------------")

        # Save the file to given path. 
        full_filename = os.path.join(PATH, submission.title)
        urllib.request.urlretrieve(submission.url, full_filename + file_type)
        pass

    time.sleep(1)
    pass
print("End of parse. ")
print("")
