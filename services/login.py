import praw
import os

def login():
    r =    praw.Reddit(username = os.getenv("reddit_username"),
        password = os.getenv("reddit_password"),
        client_id = os.getenv("client_id"),
        client_secret = os.getenv("client_secret"),
        user_agent = "WannabeQuadrilingual's BrozzerAbdullahBot v3.0")
    print("Logged in")
    return r