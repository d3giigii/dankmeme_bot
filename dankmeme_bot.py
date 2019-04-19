#!/usr/bin/python

import praw
import urllib.request
import os
import time
import datetime
import re

# Invalid characters
invalid_chars = ("<", ">", ":", "\"", "\/", "\\", "|", "?", "*")


# Path to save images to. 
PATH = "E:\\Media\\Pictures\\Memes\\Dankmemes"

# Get bot data and subreddit instance. 
reddit = praw.Reddit('BOT')
subreddit = reddit.subreddit('dankmemes')

print("")
print("Bot running. Parsing posts...")
print("")

# Iterate through posts in hot section of subreddit. Only iterates limit number of times. 
for submission in subreddit.hot(limit=60):
    valid_types = (".jpg", ".png") 
    url_string = str(submission.url) 
    title = str(submission.title)
    safe_title = re.sub('\?', '', title)
    safe_title = re.sub('*', '', title)
    print(safe_title)

    if url_string.endswith(valid_types):
        # Get file type as string. 
        file_type = url_string[-4:]

        # Print title and url of submission in console. 
        print("Title: " + title)
        print("URL  : " + submission.url)
        print("-------------------------------------------")

        # Save the file to given path. 
        full_filename = re.sub('\?', '', os.path.join(PATH, title)) 
        urllib.request.urlretrieve(submission.url, full_filename + file_type)

        # Add title and url to log file. 
        try:
            log_file = open("log.txt", "x")
        except FileExistsError:
            log_file = open("log.txt", "a")
        log_file.write("[" + str(datetime.datetime.now()) + "] " + title + " : " + url_string + "\n")
        pass
    pass
    
print("End of parse. ")
print("")
