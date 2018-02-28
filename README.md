# Spade

### Dependencies
Use `pip` to download and install these packages:
* `sqlalchemy`
* `sqlalchemy-migrate`
* `nltk`
* `tqdm` (temporary, this dependency will likely be removed in the future as this module is only used for testing purposes)
* `tweepy` (for testing with twitter comments)

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

Contains the database schema and other database code. The most important file is `models.py`, which is the python representation of the database schema. For information on how to update the database schema, refer to the section below.

##### `src.processing` module

`indexer.py` exposes a general indexer object and some basic implementations.
`index.py` will likely be obsolete once `indexer.py` reaches a functional level. The index data will simply be stored in the Indexer object, and Latent Semantic Analysis will be performed on that data.
`lsa.py` contains the algorithm for grouping documents based on topic and word occurrence. The algorithm currently uses KMeans clustering, but this should hopefully change in the future (reference: [Issue #6](https://github.com/sam-xif/Spade/issues/6)).
`queryprocessor.py` exposes a class for performing queries on the documents that have been processed by the `Index` and `LSA` classes.

##### `migrate_repo`

This directory contains the data used by `sqlalchemy-migrate` to keep track of version history of the database schema.

#### Updating the Database Schema

If you have made a change to `models.py`, then you must commit the changes to the migration repository for the database. To do this, run `<python_exec> make_migration.py --python-exec <python_exec> <message>`, where `<python_exec>` is the name of the Python 3 executable on your system and `<message>` is a short description of the changes made in the migration. After this has been run and no errors were generated, run `<python_exec> manage.py upgrade`, and the database will be upgraded. If there is content in the database, then migrating may sometimes cause problems, and `manage.py` will notify you if there are any. If the data in the database is not sensitive and you wish to avoid issues when upgrading, run `rebuild_db.bat` on Windows or `rebuild_db.sh` on Mac/Linux to create an empty database that has the most recent schema.
