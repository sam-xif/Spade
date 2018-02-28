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
        matched_docs = []
        for i, l in enumerate(self.lsa.km.labels_):
            if l == cluster:
                matched_docs.append(i)

        matched_docs.sort(key=lambda x: self.match_score(self.lsa.km.cluster_centers_[cluster], self.lsa.matrix[x], ind.documents[x], c), reverse=True)
        results = [ind.documents[i] for i in matched_docs]

        return results

    def match_score(self, centroid, data_pt, document, query_doc):
        # Tune as necessary
        a = 0.3
        b = 0.7

        dist = 1 / (1 + sqrt(sum([(x[1] - x[0])**2 for x in list(zip(centroid, data_pt))]))) # higher is better, 1 is added to denominator for normalization
        word_match = len(set(document.words) & set(query_doc.words)) # higher is better

        return a * dist + b * word_match
        # Also include in this function the level of word similarity between the query and the document, with some hyperparameters to tune the weighting
