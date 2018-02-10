# Spade

### Dependencies
Use `pip` to download and install these packages:
* `sqlalchemy`
* `sqlalchemy-migrate`
* `nltk`

Search for these packages online (install script coming soon):
* `sed` command (optional, needed in order to run `rebuild_db.bat`)

### Description

#### Goal for the Project

The main part of this project is the search engine. The search algorithm begins with processing of the text documents by tokenizing them, removing stopwords, and generating a tf-idf matrix.
The matrix stores data about the weighting of various words in each document. K-means clustering is then run on the matrix, which produces a set of "topics," with similar words and similar documents grouped together.
A search query can then be treated like a document and can be processed in the same way. Whatever cluster the word vector fits into will be where the query response is generated.

The second part of this project will be an implementation of a deterministic way to locate snippets of text on a webpage. The search index is to be populated by these snippets.

#### Code Architecture
##### `src.db` module

Contains the database schema and other database code

##### `src.processing` module

`indexer.py` exposes a general indexer object and some basic implementations.
`index.py` will likely be obsolete once `indexer.py` reaches a functional level. The index data will simply be stored in the Indexer object, and Latent Semantic Analysis will be performed on that data.

##### `migrate_repo`

This directory contains the data used by `sqlalchemy-migrate` to keep track of version history of the database schema.