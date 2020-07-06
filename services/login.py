import praw
import config

def login():
    r =    praw.Reddit(username = config.reddit_username,
        password = config.reddit_password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "WannabeQuadrilingual's BrozzerAbdullahBot v3.0")
    print("Logged in")
    return r