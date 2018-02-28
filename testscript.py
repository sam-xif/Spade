"""
testscript.py

Tests the code I have so far
"""


import sys

from src.processing.index import Index
from src.processing.lsa import LSA
import numpy as np

import src.util.twitter_scraper as twitter_scraper

ind = twitter_scraper.get_tweet_stream('trump')

f = open("testcomments.txt", "r", encoding="utf-8")
#lines = f.readlines()
#lines = [l for l in lines if l != '\n']

#ind = Index()
#for l in lines:
#    ind.index(l)

lsa = LSA(ind)
words = set()

#for d in lsa.index.documents:
#    words.update(d.words)

#for w in words:
#    print("{} : {}".format(w, lsa.tfidf_all(w)).encode('ascii', errors='replace').decode('ascii', errors='replace'))
#np.set_printoptions(threshold=np.inf)
#print(str(lsa.generate_tfidf_matrix()[1]).encode('ascii', errors='replace').decode('ascii', errors='replace'))

lsa.generate_tfidf_matrix()
np.savetxt("arr.txt", lsa.matrix)

km = lsa.cluster(num_clusters=5)
tuples = sorted(list(zip(km.labels_, lsa.word_list)), key=lambda x: x[0])
#print(str(tuples).encode('ascii', errors='replace').decode('ascii', errors='replace'))

km = lsa.cluster(num_clusters=2, t=True)
print(km.labels_)

from src.processing.queryprocessor import QueryProcessor
qp = QueryProcessor(lsa)
res = qp.query("election")
#print([r.words for r in res])
#for i, data_pt in enumerate(lsa.matrix):
    #print(lsa.word_list[i], data_pt)
#print(res)

#from src.db.dbcontroller import DBController
#dbc = DBController('sqlite+pysqlite:///spade.db', DEBUG=True)
#lsa.generate_tfidf_matrix()
#lsa.save_to_db(dbc)
