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

print(lsa.tfidf_all(sys.argv[1]))