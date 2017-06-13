#!/usr/bin/python
import praw
from vadersentiment import SentimentIntensityAnalyzer
from nltk import tokenize
frontPageSize = 25
subreddits = ["ethereum", "ethtrader", "ripple", "bitcoin", "btc"]
reddit = praw.Reddit('bot1')
analyzer = SentimentIntensityAnalyzer()

##Static methods##

def get_sentiment_from_paragraph(paragraph):
    sentence_list = tokenize.sent_tokenize(paragraph)
    paragraphSentiments = 0.0
    for sentence in sentence_list:
        vs = analyzer.polarity_scores(sentence)
        paragraphSentiments += vs["compound"]
    return round(paragraphSentiments/len(sentence_list), 4)

def get_sentiment_from_subreddit(subredditName):
    subreddit = reddit.subreddit(subredditName)
    subredditSentiments = 0.0
    submissions = subreddit.hot(limit=frontPageSize)
    for submission in submissions:
        titleSentiment = get_sentiment_from_paragraph(submission.title)
        subredditSentiments += titleSentiment
    return round(subredditSentiments/frontPageSize, 4)

##Entry##

for subredditName in subreddits:
    print("Subreddit: ", subredditName)
    print("Sentiment: ", get_sentiment_from_subreddit(subredditName))
    print("---------------------------------\n")
