"""
testscript.py

Tests the code I have so far
"""


import sys

from src.processing.index import Index
from src.processing.lsa import LSA

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

for w in words:
    print("{} : {}".format(w, lsa.tfidf_all(w)).encode('utf-8').decode('ascii', errors='replace'))
    
    
#print(lsa.tfidf_all(sys.argv[1]))