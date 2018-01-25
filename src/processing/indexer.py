"""
indexer.py
"""

import nltk
from nltk.tokenize.punkt import word_tokenize
from src.processing.index import Index

class Indexer:
    """
    Indexer interface
    """
    
    def index(self, data):
        """
        Main indexing function
        """
        pass

class POSIndexer(Indexer):
    def __init__(self):
        self.index = Index()

    def index(self, data):
        # The data is expected to be text
        words = word_tokenize(data)
        pos_tagged_words = nltk.pos_tag(words)