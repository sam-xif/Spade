"""
queryprocessor.py
"""

from src.processing.lsa import LSA
from src.processing.index import Index

class QueryProcessor:
    def __init__(self, lsa):
        self.lsa = lsa
        pass

    def build_from_db(self, dbcontroller):
        pass

    def query(self, query_string):
        ind = Index()
        c = ind.preprocess(query_string)
        tfidf_vals = self.lsa.tfidf_all(c)
        cluster = lsa.km.predict(tfidf_vals)

        # Get all documents in this cluster
