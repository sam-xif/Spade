"""
index.py
"""

import nltk
import re
from nltk.tokenize import TweetTokenizer

#from nltk.tokenize.punkt import word_tokenize
#from index import Index

from nltk.corpus import stopwords
from src.db.comment import Comment
from nltk.stem.porter import *
        
class Index:
    def __init__(self):
        self.documents = []

    def index(self, data):
        # The data should be raw text
        c = self.preprocess(data)
        self.documents.append(c)
        
    def size(self):
        return len(self.documents)
        
    def preprocess(self, document):
        # Tweet tokenize
        # Remove stopwords
        # Porter stemmer
        
        tok = TweetTokenizer(strip_handles=True, reduce_len=True)
        words = [w.lower() for w in tok.tokenize(document)] # Tokenize the document and make all the words lowercase
        stopWords = stopwords.words('english')
        
        # Remove stopwords
        words = [w for w in words if w not in stopWords]
        
        words = [w for w in words if re.match(r'^[.,\/#!$%\^&\*;:{}=\-_`~()]$', w) == None]
        
        # Separate text into hashtags and actual text
        c = Comment(words)
        
        # Stem the words
        stemmer = PorterStemmer()
        c.words = [stemmer.stem(w) for w in c.words]
        
        return c