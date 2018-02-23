"""
lsa.py
Module that performs clustering using latent semantic analysis on a group of comments
"""

from math import log
from src.processing.index import Index
from nltk.stem.porter import *
import numpy as np
from src.db.dbcontroller import DBController
from src.db.models import *

from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

class LSA:
    def __init__(self, index):
        self.index = index
        self.word_list = self.generate_word_list()

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

    def cluster(self, num_clusters=5):
        print(self.matrix.shape)
        km = KMeans(n_clusters=num_clusters)
        km.fit(self.matrix)
        self.km = km
        return km

    def generate_word_list(self):
        words = set()

        for d in self.index.documents:
            words.update(d.words)

        word_list = list(words)
        return word_list

    def generate_tfidf_matrix(self):
        if self.word_list is None:
            raise Error('word_list is None')
        matrix = []
        for w in self.word_list:
            matrix.append(self.tfidf_all(w))

        self.matrix = np.array(matrix)

    def save_to_db(self, dbcontroller):
        #word_list, matrix = self.generate_tfidf_matrix()
        with dbcontroller as session:
            for i, word in enumerate(self.word_list):
                t = Term(text=word)
                session.add(t)
                for j, document in enumerate(self.index.documents):
                    d = Document(words=str(list(document.words)), tags=str(list(document.tags)), raw=str(document.raw))
                    session.add(d)

                    tfidf_entry = TFIDF(document=d, term=t, tfidf_value=self.matrix[i][j])
                    session.add(tfidf_entry)

            session.commit()

    def build_from_db(self, dbcontroller):
        self.index.build_from_db(dbcontroller)
        with dbcontroller as session:
            tfidf_data = session.query(TFIDF).all()
