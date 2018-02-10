"""
testscript.py

Tests the code I have so far
"""


import sys

from src.processing.index import Index
from src.processing.lsa import LSA
import numpy as np

f = open("testcomments.txt", "r", encoding="utf-8")
lines = f.readlines()
lines = [l for l in lines if l != '\n']

ind = Index()
for l in lines:
    ind.index(l)
    
lsa = LSA(ind)
words = set()

for d in lsa.index.documents:
    words.update(d.words)

#for w in words:
#    print("{} : {}".format(w, lsa.tfidf_all(w)).encode('ascii', errors='replace').decode('ascii', errors='replace'))
#np.set_printoptions(threshold=np.inf)
#print(str(lsa.generate_tfidf_matrix()[1]).encode('ascii', errors='replace').decode('ascii', errors='replace'))

mat = lsa.generate_tfidf_matrix()
np.savetxt("arr.txt", lsa.generate_tfidf_matrix()[1]) 

km = lsa.cluster(mat[1], num_clusters=7)
tuples = sorted(list(zip(km.labels_, mat[0])), key=lambda x: x[0])
print(str(tuples).encode('ascii', errors='replace').decode('ascii', errors='replace'))

km = lsa.cluster(mat[1].T)
print(km.labels_)