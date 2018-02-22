# Changelog

### Jan 22, 2018

Initial commit

### Jan 23, 2018

Began formulating basic code architecture.

### Jan 25, 2018

Added a system for managing the database and migrations between different versions of the schema.
Organizing file hierarchy and continuing to devise a plan for the code architecture based on research.

### Jan 27, 2018

Merged Jocelyn's pull request to add a code of conduct, and updated it slightly.

### Jan 29, 2018

Merged Miles's pull request which added a `requirements.txt` file, which is the file where `pip` looks for dependencies.
Also updated the README file with additional information.

### Jan 30, 2018

Created the first iteration of the database schema

### Feb 2, 2018

Began development of the indexer that will be used to index comments.

### Feb 6, 2018

Continue developing the index module. Made changes to README as well.

### Feb 7, 2018

Restructured he index module and added the latent semantic analysis module.

### Feb 8, 2018

Created this changelog.

### Feb 19, 2018

Fixed `make_migration.py` and added a version of `rebuild_db.bat` for Bash (`rebuild_db.sh`).
Additionally, added more database models to facilitate the storage of tf-idf matrices.

### Feb 20, 2018

Added the `DBController` class, which allows for easy access to adding to and querying the database.

### Feb 22, 2018

Finished `DBController` and added functionality to save the tf-idf matrix to the database.
Started work on the query processor module.
