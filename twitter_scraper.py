import tweepy
from nltk.stem.porter import PorterStemmer
import re
from collections import Counter
import pandas as pd

def get_api():
    c_key = input("Consumer key: ")
    c_secret = input("Consumer secret: ")
    a_key = input("Access token: ")
    a_secret = input("Access token secret: ")
    auth = tweepy.OAuthHandler(c_key, c_secret, "https://google.com")
    auth.set_access_token(a_key, a_secret)
    api = tweepy.API(auth)
    return api

def get_tweet_stream(keyword):
    tweets = []
    for i in tweepy.Cursor(get_api().search, q=keyword).items(25):
        tweets.append(i.text.encode("utf-8"))
    df = pd.DataFrame(tweets, columns = ['Tweet'])
    df.to_csv("twitter_data.csv")
    return df

print(get_tweet_stream('dog'))
