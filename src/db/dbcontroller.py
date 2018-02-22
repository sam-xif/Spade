"""
dbcontroller.py
"""
import sys
import os
if __name__=='__main__':
    sys.path.append(os.path.realpath('../../'))


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlite3 import dbapi2 as sqlite

CONNECT_STRING='sqlite+pysqlite:///../../spade.db'

class DBController:
    """
    Allows for easy adding of documents, terms, and tf-idf data to the database.
    Also exposes a query API to efficiently search through the comments.

    How the search algorithm will work:

    First, a tf-idf matrix of the set of documents will be recalled.
    KMeans clustering will be run on it, and the search query will be treated as an extra document in the tf-idf matrix.
    Based on the cluster the query gets assigned to, documents will be selected and ordered based on match distance,
     which is a function that somehow defines the "distance" between two documents.

    TODO: Modify the above statement, which doesn't accurately describe this class

    Usage:
    dbcon = DBController()
    # To create a new session:
    with dbcon as session:
        session.query(...)
        session.add(...)
        session.commit()

    # Repeat to create more sessions

    """

    def __init__(self, connect_string, DEBUG=False):
        self.engine = create_engine(connect_string, module=sqlite, echo=DEBUG)
        self.Session = sessionmaker(bind=self.engine)
        self.active_session = None

    def __enter__(self):
        # Whenever enter is called, create a new session and make it the active session
        self.active_session = self.Session()
        return self.active_session

    def __exit__(self, type, value, traceback):
        # Close down the database stuff
        if self.active_session is not None:
            self.active_session.close() # Maybe wrap this with a try statement
            self.active_session = None

        return isinstance(value, Exception)


    def destroy(self):
        # Unbind the engine here if needed
        pass
