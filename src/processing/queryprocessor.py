"""
queryprocessor.py
"""

from src.processing.lsa import LSA
from src.processing.index import Index
from math import *

class QueryProcessor:
    def __init__(self, lsa):
        self.lsa = lsa

    def build_from_db(self, dbcontroller):
        pass

    def query(self, query_string):
        # TODO: look into expanding this to support an array of queries at once
        ind = self.lsa.index
        c = ind.preprocess(query_string)
        tfidf_vals = self.lsa.tfidf_document(c)
        cluster = self.lsa.km.predict(tfidf_vals.reshape(1, -1))[0]
        print(self.lsa.km.cluster_centers_)
        matched_docs = []
        for i, l in enumerate(self.lsa.km.labels_):
            if l == cluster:
                matched_docs.append(i)

        print(cluster)
        print(matched_docs)
        matched_docs.sort(key=lambda x: self.match_distance(self.lsa.km.cluster_centers_[cluster], self.lsa.matrix[x]))
        print(matched_docs)
        results = [ind.documents[i].words for i in matched_docs]

        return results
        # Get all documents in this cluster:
        # - Get all (term, document) pairs that are in the same cluster as the query
        # - Get the set of all the documents contained within this points.
        # Order the set by match distance (some function that I haven't defined yet) between the query and each returned document
        # Return this set

    def match_distance(self, centroid, data_pt):
        return sqrt(sum([(x[1] - x[0])**2 for x in list(zip(centroid, data_pt))])) # Also include in this function the level of word similarity between the query and the document, with some hyperparameters to tune the weighting
