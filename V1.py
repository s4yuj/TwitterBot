import tweepy
import praw
import random
import os

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     username="",
                     password="",
                     user_agent="",
                     check_for_async=False)

subreddit = reddit.subreddit(SUBREDDITNAME)
allposts = []
top = subreddit.top(limit=400)
for submission in top:
    words=submission.title.split(' ')
    if len(words)<20:
        allposts.append(submission)
print(allposts)

randpost= random.choice(allposts)
post = randpost.title
# url = randpost.url
# media=randpost.media_embed

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)
if __name__=='__main__':
    try:
        api.update_status(status=post)
        print('tweeted')
    except (tweepy.error.TweepError):
        allposts.remove(post)
        api.update_status(status=post)
