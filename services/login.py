import praw
import os
from dotenv import load_dotenv #for reading the .env file and putting the credentials in environment variables

def login():
    load_dotenv()
    r =    praw.Reddit(username = os.getenv("reddit_username"),
        password = os.getenv("reddit_password"),
        client_id = os.getenv("client_id"),
        client_secret = os.getenv("client_secret"),
        user_agent = "WannabeQuadrilingual's BrozzerAbdullahBot v3.0")
    print("Logged in")
    return r