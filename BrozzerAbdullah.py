# -*- coding: utf-8 -*-
import praw
import config
import time
import re
import logging
import sys
from responseService.quranVerseResponse import getQuranVerse
from constants import constants
from random import randint
from linereader import copen

def bot_login():
    print("Logging in...")
    r =    praw.Reddit(username = config.reddit_username,
        password = config.reddit_password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "WannabeQuadrilingual's BrozzerAbdullahBot v3.0")
    print("Logged in")
    return r


def run_bot(r):
    comment_stream = r.subreddit(constants.subreddits).stream.comments(pause_after=-1,skip_existing=True)
    submission_stream = r.subreddit(constants.subreddits).stream.submissions(pause_after=-1,skip_existing=True)
    while True:
        for comment in comment_stream:
            if (comment is None):
                break
            comment_text = comment.body.lower()
            reply_comment = ""
            searchObj = re.search( r'-qur\'?an \b([1][0,1][0,1,2,3,4]|[1-9][0-9]?)\b:([0-9]{1,3})\b-?(\b([0-9]{1,3})\b)?', comment_text, re.I)

            if(searchObj):
                reply_comment = getQuranVerse(searchObj)
            else:
                if("good bot" in comment_text and comment.parent().author == r.user.me()):
                    print ("Found good bot in https://www.reddit.com" + comment.permalink)
                    reply_comment = "Good Human. " + get_random_dua() + "\n\n"
                if("bad bot" in comment_text and comment.parent().author == r.user.me()):
                    print ("Found bad bot in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + "[Behave yourself!](https://i.ytimg.com/vi/oL15on_OyBA/hqdefault.jpg)\n\n"
                if any(takbir in comment_text for takbir in constants.takbirList) and comment.subreddit in ['Izlam','izlanimemes']:
                    print ("Found Takbir in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + "#الله اكبر  ALLAHU AKBAR!!!!\n\n"
                if any(taqiya in comment_text for taqiya in constants.taqiyaList) and not comment.author == r.user.me() and comment.subreddit in ['Izlam','izlanimemes']:
                    print ("Found Taqiya in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + "This brozzer/sizter is using taqqiya, 100% true taqqiya master\n\n"
                if ("staff gorilla" in comment_text and comment.subreddit in ['Izlam','izlanimemes']):
                    print ("Found staff gorilla in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + "[You called me?](https://imgur.com/T60vscc)\n\n"
                if any(jazakallah in comment_text for jazakallah in constants.jazakallahList) and comment.parent().author == r.user.me():
                    print ("Found jazakallah in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + "وأنتم فجزاكم الله خيرا Wa antum, fa jazakumullahu khairan\n\n"
            if reply_comment!="":
                print ("Replying to comment : " + comment.body)
                reply_comment = reply_comment + constants.footer
                comment.reply(reply_comment)
        for submission in submission_stream:
            if(submission is None):
                break
            submission_text = submission.title.lower() + "------\n" + submission.selftext.lower()
            reply_comment = ""
            if any(taqiya in submission_text for taqiya in constants.taqiyaList) and submission.subreddit in ['Izlam','izlanimemes']:
                print("Taqiya in Post : " + submission.permalink)
                reply_comment = "Sniff, sniff... I smell Taqiya\n\n"
            if any(takbir in submission_text for takbir in constants.takbirList) and submission.subreddit in ['Izlam','izlanimemes']:
                print ("Found Takbir in " + submission.permalink)
                reply_comment = reply_comment + "#الله اكبر  ALLAHU AKBAR!!!!\n\n"
            if ("staff gorilla" in submission_text) and submission.subreddit in ['Izlam','izlanimemes']:
                print ("Found staff gorilla in " +submission.permalink)
                reply_comment = reply_comment + "[You called me?](https://imgur.com/T60vscc)\n\n"
            if reply_comment!="":
                print ("Replying to comment : " + submission.permalink)
                reply_comment = reply_comment + constants.footer
                submission.reply(reply_comment)


def get_random_dua():
    openfile = copen("./constants/dua.txt")
    lines = openfile.count('\n') + 1
    dua = openfile.getline(randint(1,lines))
    return dua

r = bot_login()
while True:
    run_bot(r)
