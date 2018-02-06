"""
index.py
"""

from indexer import BasicIndexer

class Index:
    """
    An implementation of an inverted index
    """

    def __init__(self, indexer_object=BasicIndexer):
        self.word_map = {} # Maps words to documents
        self.tag_map = {} # Maps tags to documents
        self.indexer_object = indexer_object
        
    def preprocess(self, document):
        pass
        
    def add_document(self, document):
        processor = self.indexer_object()
        processor.index(self.preprocess(document))
        
        pass