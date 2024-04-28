import praw
import pandas as pd
import json

subreddit_name = 'leafs'

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    CLIENT_ID = config['CLIENT_ID']
    CLIENT_SECRET = config['CLIENT_SECRET']
    USER_AGENT = config['USER_AGENT']

def credentials(client_id, client_secret, user_agent):
    return praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)


def fetch_posts(subreddit_name, limit=5):
    posts = credentials('your_client_id', 'your_client_secret', 'your_user_agent')
    subreddit = posts.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):
        content = post.title + ' ' + post.selftext
        posts.append(content)
        post.comments.replace_more(limit=5)
        for comment in post.comments.list():
            posts.append(comment.body)

    return posts
