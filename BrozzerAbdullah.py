# -*- coding: utf-8 -*-
import re
from services.quranVerseResponse import getQuranVerse
from responseConstants import constants
from services.login import login
import services.generalResponses as responses

def run_bot(r):
    comment_stream = r.subreddit(constants.subreddits).stream.comments(pause_after=-1,skip_existing=True)
    submission_stream = r.subreddit(constants.subreddits).stream.submissions(pause_after=-1,skip_existing=True)
    while True:
        for comment in comment_stream:
            if (comment is None or comment.author == r.user.me()):
                break
            comment_text = comment.body.lower()
            reply_comment = ""
            quranObject = re.finditer( r'-qur\'?an \b([1][0,1][0,1,2,3,4]|[1-9][0-9]?)\b:([0-9]{1,3})\b-?(\b([0-9]{1,3})\b)?', comment_text, re.I)
            for match in quranObject:
                reply_comment = getQuranVerse(match,reply_comment)
            if (reply_comment == ""):
                if("-info" in comment_text and comment.parent().author == r.user.me()):
                    # print ("Found info in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + responses.infoResponse()                
                if("good bot" in comment_text and comment.parent().author == r.user.me()):
                    # print ("Found good bot in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + responses.goodBotResponse()
                if("bad bot" in comment_text and comment.parent().author == r.user.me()) and comment.subreddit in ['Izlam','izlanimemes','MTN']:
                    # print ("Found bad bot in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + responses.badBotResponse()
                if any(takbir in comment_text for takbir in constants.takbirList) and comment.subreddit in ['Izlam','izlanimemes','MTN']:
                    # print ("Found Takbir in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + responses.takbirResponse() 
                if any(taqiya in comment_text for taqiya in constants.taqiyaList) and comment.subreddit in ['Izlam','izlanimemes','MTN']:
                    # print ("Found Taqiya in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + responses.taqiyaResponse() 
                if ("staff gorilla" in comment_text and comment.subreddit in ['Izlam','izlanimemes','MTN']):
                    # print ("Found staff gorilla in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + responses.staffGorillaResponse() 
                if any(jazakallah in comment_text for jazakallah in constants.jazakallahList) and comment.parent().author == r.user.me():
                    # print ("Found jazakallah in https://www.reddit.com" + comment.permalink)
                    reply_comment = reply_comment + responses.jazakallahResponse() 
            if reply_comment!="":
                print ("Replying to comment : " + comment.body)
                reply_comment = reply_comment + constants.footer
                comment.reply(reply_comment)
        for submission in submission_stream:
            if(submission is None):
                break
            submission_text = submission.title.lower() + "------\n" + submission.selftext.lower()
            reply_comment = ""
            quranObject = re.finditer( r'-qur\'?an \b([1][0,1][0,1,2,3,4]|[1-9][0-9]?)\b:([0-9]{1,3})\b-?(\b([0-9]{1,3})\b)?', submission_text, re.I)
            for match in quranObject:
                reply_comment = getQuranVerse(match,reply_comment)
            if (reply_comment == ""):
                if any(taqiya in submission_text for taqiya in constants.taqiyaList) and submission.subreddit in ['Izlam','izlanimemes','MTN']:
                    # print("Taqiya in Post : " + submission.permalink)
                    reply_comment = reply_comment + responses.taqiyaPostResponse() 
                if any(takbir in submission_text for takbir in constants.takbirList) and submission.subreddit in ['Izlam','izlanimemes','MTN']:
                    # print ("Found Takbir in " + submission.permalink)
                    reply_comment = reply_comment + responses.takbirResponse() 
                if ("staff gorilla" in submission_text) and submission.subreddit in ['Izlam','izlanimemes','MTN']:
                    # print ("Found staff gorilla in " +submission.permalink)
                    reply_comment = reply_comment + responses.staffGorillaResponse() 
            
            if reply_comment!="":
                print ("Replying to comment : " + submission.submission_text)
                reply_comment = reply_comment + constants.footer
                submission.reply(reply_comment)

r = login()
while True:
    run_bot(r)
