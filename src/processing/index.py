"""
index.py
"""

import nltk
import re
from nltk.tokenize import TweetTokenizer

#from nltk.tokenize.punkt import word_tokenize
#from index import Index

from nltk.corpus import stopwords
from src.db.document import Document
from nltk.stem.porter import *
import src.db.models as models

class Index:
    def __init__(self, custom_stopwords=[]):
        self.documents = []
        self.custom_stopwords = custom_stopwords

    def index(self, data):
        # The data should be raw text
        c = self.preprocess(data)
        self.documents.append(c)

    def index_range(self, data):
        for doc in data:
            self.index(doc)

    def size(self):
        return len(self.documents)

    def preprocess(self, document):
        # Tweet tokenize
        # Remove stopwords
        # Porter stemmer

        tok = TweetTokenizer(strip_handles=True, reduce_len=True)
        words = [w.lower() for w in tok.tokenize(document)] # Tokenize the document and make all the words lowercase
        stopWords = stopwords.words('english')

        url_re = r'(http(s)?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'

        # Remove stopwords
        words = [w for w in words if w not in stopWords]

        if len(self.custom_stopwords) > 0:
            words = [w for w in words if w not in self.custom_stopwords]

        # Remove punctuation and empty strings
        words = [w for w in words if re.match(r'^[.,\/#!?$%\^&\*;:{}=\-_`~()"\']*$', w) is None]

        # Remove url strings
        words = [w for w in words if re.match(url_re, w) is None]

        # Separate text into hashtags and actual text
        c = Document.create_from_raw_list(words, document)

        # Stem the words
        stemmer = PorterStemmer()
        c.words = [stemmer.stem(w) for w in c.words]

        return c

    def build_from_db(self, dbcontroller):
        with dbcontroller as session:
            db_documents = session.query(models.Document).all()
            self.documents = [Document.create_from_raw_list(x.words, x.tags, x.raw) for x in db_documents]
