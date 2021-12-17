import tweepy
import praw
import os
import random
import time
from datetime import datetime
import pytz

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     username="",
                     password="",
                     user_agent="",
                     check_for_async=False)

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

subreddit=reddit.subreddit('science')
hot_science=subreddit.hot(limit=30)

subreddit=reddit.subreddit('technology')
hot_tech=subreddit.hot(limit=30)

hot= list(hot_tech) + list(hot_science)
random.shuffle(hot)

def checkUnique(text):
    with open('test.txt','r') as f:
        contents=f.read()
        if str(text) in contents:
            return False
        else:
            return True

def addpost(post):
    with open('test.txt','a') as f:
        f.write(f'{post}\n')

def makePost():    
    while True:
        for submission in hot:
            chars=list(submission.title)+list(submission.url)+list(submission.link_flair_text)
            if (checkUnique(submission.title)==True) and (len(chars)<280) and (submission.score>1500) and (submission.upvote_ratio>0.75):
            # print(submission.title,submission.score, submission.upvote_ratio, submission.link_flair_text, submission.url, sep='\n')
                post=submission.title
                link=submission.url
                flair=submission.link_flair_text.upper()

                data=f'{flair}: {post}\n\n{link}\n'
                api.update_status(status=data)
                print('tweeted')
                print(data)
                addpost(post)
                break
        break

# while True:
#     makePost()
#     time.sleep(1800)

tz_ND = pytz.timezone('India/New_Delhi') 
datetime_NY = datetime.now(tz_ND)