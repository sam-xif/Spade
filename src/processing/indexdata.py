"""
indexdata.py

Exposes an interface for data that should be passed into the indexer
"""

class IndexData:
    def __init__(self, data, **kwargs):
        self.data = data    