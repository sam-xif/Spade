"""
indexer.py

(This file may be obsolete)
"""

import nltk
from nltk.tokenize import TweetTokenizer

#from nltk.tokenize.punkt import word_tokenize
#from index import Index

from nltk.corpus import stopwords
from src.db.comment import Comment
from nltk.stem.porter import *

class Indexer:
    """
    Indexer interface
    """
    
    def index(self, data):
        """
        Main indexing function
        """
        pass
        
    def preprocess(self, document):
        pass
        
class BasicIndexer(Indexer):
    def __init__(self):
        self.documents = []

    def index(self, data):
        # The data should be raw text
        c = self.preprocess(data)
        self.documents.append(c)
        
    def preprocess(self, document):
        # Tweet tokenize
        # Remove stopwords
        # Porter stemmer
        
        tok = TweetTokenizer(strip_handles=True, reduce_len=True)
        words = [w.lower() for w in tok.tokenize(document)] # Tokenize the document and make all the words lowercase
        stopwords = stopwords.words('english')
        
        # Remove stopwords
        words = [w for w in words if w not in stopwords]
        
        # Separate text into hashtags and actual text
        c = Comment(words)
        
        # Stem the words
        stemmer = PorterStemmer()
        c.words = [stemmer.stem(w) for w in c.words]
        
        return c

class POSIndexer(Indexer):
    def __init__(self):
        pass

    def index(self, data):
        # As of now, the data is expected to be text
        tok = TweetTokenizer(strip_handles=True, reduce_len=True)
        words = tok.tokenize(data)
        pos_tagged_words = nltk.pos_tag(words)
        
        
        print(pos_tagged_words)
