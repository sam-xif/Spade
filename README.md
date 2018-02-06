# Spade

### Dependencies
Use `pip` to download and install these packages:
* `sqlalchemy`
* `sqlalchemy-migrate`
* `pysqlite`
* `nltk`
* `bs4` (`beautifulsoup4`)

Search for these packages online (install script coming soon):
* `sed` command (in order to run `rebuild_db.bat`)

### Description

#### Code Architecture
* `src.db` module
Contains the database schema and other database code
* `src.processing` module
`indexer.py` exposes a general indexer object and some basic implementations.
`index.py` will likely be obsolete once `indexer.py` reaches a functional level. The index data will simply be stored in the Indexer object, and Latent Semantic Analysis will be performed on that data.