#Twitter Scrape
import tweepy
from nltk.stem.porter import PorterStemmer
import re
from collections import Counter
import pandas as pd
from src.processing.index import Index
from src.processing.lsa import LSA

def get_api():
    a = open('keys.txt')
    c_key, c_secret, a_key, a_secret = a.read().split("\n")[0:4]
    auth = tweepy.OAuthHandler(c_key, c_secret, "https://google.com")
    auth.set_access_token(a_key, a_secret)
    api = tweepy.API(auth)
    return api

def get_tweet_stream(keyword):
    tweets = []
    for i in tweepy.Cursor(get_api().search, q=keyword).items(200):
        tweets.append(i.text.encode("utf-8").decode("ascii", errors='ignore'))

    ind = Index(custom_stopwords=['rt'])
    ind.index_range(tweets)
    return ind

def get_index(df):
    a = Index()
    tweet_contents = df['Tweet'].values
    tweet_contents = [(x.decode('utf-8')) for x in tweet_contents]
    tweets_cleaned = []
    for tweet in tweet_contents:
        tweet = a.index(tweet)
        tweets_cleaned.append(tweet)                    #Fix str/byte error
    df_=pd.DataFrame(tweets_cleaned)
    print(a.documents)
    #df_.to_csv("twitter_data.csv")
    return a

def get_tfidf_matrix(index):
    l = LSA(index)
    return l.generate_tfidf_matrix()
