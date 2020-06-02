# -*- coding: utf-8 -*-
import praw
import config
import time
import re
import logging
import sys
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
    takbirList = ['takbir','takbeer','tekbir','تكبير']
    taqiyaList = ['taqiyya','taqqiyya','taqiya','taqqiya']
    jazakallahList = ['jazakallah','jazakillah','jazakumullah']
        
    footer = "\n^[r/MuslimDevNetwork](https://www.reddit.com/r/MuslimDevNetwork/) ^|| ^[r/Sahaba](https://www.reddit.com/r/Sahaba/) ^|| ^[r/MuslimLounge](https://www.reddit.com/r/MuslimLounge/)"

    comment_stream = r.subreddit('Izlam').stream.comments(pause_after=-1)
    submission_stream = r.subreddit('Izlam').stream.submissions(pause_after=-1)
    while True:
        for comment in comment_stream:
            if (comment is None):
                break
            comment_text = comment.body.lower()
            reply_comment = ""
            if("good bot" in comment_text and comment.parent().author == r.user.me()):
                    # logging.info ("Found good bot in " + comment.id)
                    reply_comment = "Good Human. " + get_random_dua() + "\n\n"
            if("bad bot" in comment_text and comment.parent().author == r.user.me()):
                # logging.info ("Found bad bot in " + comment.id)
                reply_comment = reply_comment + "[Behave yourself!](https://i.ytimg.com/vi/oL15on_OyBA/hqdefault.jpg)\n\n"
            if any(takbir in comment_text for takbir in takbirList):
                # logging.info ("Found Takbir in " + comment.id)
                reply_comment = reply_comment + "#الله اكبر  ALLAHU AKBAR!!!!\n\n"
            if any(taqiya in comment_text for taqiya in taqiyaList) and not comment.author == r.user.me() :
                # logging.info ("Found Taqiya in " + comment.id)
                reply_comment = reply_comment + "This brozzer/sizter is using taqqiya, 100% true taqqiya master\n\n"
            if ("staff gorilla" in comment_text):
                # logging.info ("Found staff gorilla in " +comment.id)
                reply_comment = reply_comment + "[You called me?](https://imgur.com/T60vscc)\n\n"
            if any(jazakallah in comment_text for jazakallah in jazakallahList) and comment.parent().author == r.user.me():
                # logging.info ("Found jazakallah in " + comment.id)
                reply_comment = reply_comment + "وأنتم فجزاكم الله خيرا Wa antum, fa jazakumullahu khairan\n\n"
            if reply_comment!="":
                logging.info ("Replying to comment : " + comment.body)
                # logging.info(reply_comment)
                reply_comment = reply_comment + footer
                comment.reply(reply_comment)
        for submission in submission_stream:
            if(submission is None):
                break
            submission_text = submission.title.lower() + "------\n" + submission.selftext.lower()
            reply_comment = ""
            if any(taqiya in submission_text for taqiya in taqiyaList):
                # logging.info("Taqiya in Post : " + submission.id)
                reply_comment = "Sniff, sniff... I smell Taqiya\n\n"
            if any(takbir in submission_text for takbir in takbirList):
                # logging.info ("Found Takbir in " + submission.id)
                reply_comment = reply_comment + "#الله اكبر  ALLAHU AKBAR!!!!\n\n"
            if ("staff gorilla" in submission_text):
                # logging.info ("Found staff gorilla in " +submission.id)
                reply_comment = reply_comment + "[You called me?](https://imgur.com/T60vscc)\n\n"
            if reply_comment!="":
                logging.info ("Replying to comment : " + submission.id)
                # logging.info(reply_comment)
                reply_comment = reply_comment + footer
                submission.reply(reply_comment)


def get_random_dua():
    openfile = copen("dua.txt")
    lines = openfile.count('\n') + 1
    dua = openfile.getline(randint(1,lines))
    return dua

r = bot_login()
while True:
    run_bot(r)
