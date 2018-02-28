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
        if self.active_session is not None:
            raise Exception('There is already an active session on this controller. You cannot open another one until calling __exit__() or leaving the `with` statement block.')
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
