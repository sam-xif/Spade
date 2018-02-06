"""
indexer.py
"""

import nltk
from nltk.tokenize import TweetTokenizer
#from nltk.tokenize.punkt import word_tokenize
from index import Index

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
        pass

    def index(self, data):
        # As of now, the data is expected to be text
        pass
        
    def preprocess(self, document):
        # Tweet tokenize
        # Remove stopwords
        # Porter stemmer
        
        tok = TweetTokenizer(strip_handles=True, reduce_len=True)
        words = tok.tokenize(document)
        
        pass

class POSIndexer(Indexer):
    def __init__(self):
        pass

    def index(self, data):
        # As of now, the data is expected to be text
        tok = TweetTokenizer(strip_handles=True, reduce_len=True)
        words = tok.tokenize(data)
        pos_tagged_words = nltk.pos_tag(words)
        
        
        print(pos_tagged_words)
