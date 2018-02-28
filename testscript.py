"""
testscript.py

Tests the code I have so far
"""

import sys
from src.processing.index import Index
from src.processing.lsa import LSA
import numpy as np
import src.util.twitter_scraper as twitter_scraper
from src.processing.queryprocessor import QueryProcessor
from src.db.dbcontroller import DBController

print("fetching tweets...")
ind = twitter_scraper.get_tweet_stream('trump')
lsa = LSA(ind)
lsa.generate_tfidf_matrix()
km = lsa.cluster(num_clusters=5)
#tuples = sorted(list(zip(km.labels_, lsa.word_list)), key=lambda x: x[0])
#print(str(tuples).encode('ascii', errors='replace').decode('ascii', errors='replace'))

km = lsa.cluster(num_clusters=2, t=True)

qp = QueryProcessor(lsa)
res = qp.query("election") # print out raw documents in a nice results format
for i, doc in enumerate(res):
    print("[RESULT {}]".format(i))
    print(doc.raw)

### Uncomment for test of database functionality
#dbc = DBController('sqlite+pysqlite:///spade.db', DEBUG=False)
#lsa.save_to_db(dbc)
