"""
lsa.py
Module that performs clustering using latent semantic analysis on a group of comments
"""

from math import log
from src.processing.index import Index
from nltk.stem.porter import *
import numpy as np

from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity


class LSA:
    def __init__(self, index):
        self.index = index
        
    def tfidf(self, term, document):
        # term should be a lowercase, stemmed word
        # tfidf(t, d, D) = tf(t, d) * idf(t, D)
        
        stemmer = PorterStemmer()
        stemmed_term = stemmer.stem(term)
        
        tf = 0
        for w in document.words:
            if w == stemmed_term:
                tf += 1
                
        # Potential Issue: tfidf currently only uses the words and keeps hashtags separate. 
        # The problem is that hashtags may contain semantic significance that we are losing.
        idf = log(self.index.size() / (1 + len([d for d in self.index.documents if stemmed_term in d.words]))) 
        
        return tf * idf
        
    def tfidf_all(self, term):
        return [self.tfidf(term, doc) for doc in self.index.documents]
            
    def cluster(self, matrix, num_clusters=5):
        km = KMeans(n_clusters=num_clusters)
        km.fit(matrix)
        return km
    
    def generate_tfidf_matrix(self):
        matrix = []
        words = set()

        for d in self.index.documents:
            words.update(d.words)
        
        words_list = list(words)
        for w in words_list:
            matrix.append(self.tfidf_all(w))
            
        return words_list, np.array(matrix)
            