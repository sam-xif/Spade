#Twitter Scrape
import tweepy
from nltk.stem.porter import PorterStemmer
import re
from collections import Counter
import pandas as pd
from src.processing.index import Index

def get_api():
    a = open('keys.txt')
    c_key, c_secret, a_key, a_secret = a.read().split("\n")[0:4]
    auth = tweepy.OAuthHandler(c_key, c_secret, "https://google.com")
    auth.set_access_token(a_key, a_secret)
    api = tweepy.API(auth)
    return api

def get_tweet_stream(keyword):
    tweets = []
    for i in tweepy.Cursor(get_api().search, q=keyword).items(25):
        tweets.append(i.text.encode("utf-8"))
    df = pd.DataFrame(tweets, columns = ['Tweet'])
    df = clean(df)
    return df

def clean(df):
    a = Index()
    tweet_contents = df['Tweet'].values
    tweet_contents = [str(x.decode('utf-8')) for x in tweet_contents]
    print(tweet_contents)
    tweets_cleaned = a.preprocess(tweet_contents)                      #Fix str/byte error
    df_=pd.DataFrame(tweets_cleaned, columns = ['Tweet'])
    df_.to_csv("twitter_data.csv")
    return df_

print(get_tweet_stream('dog'))
