"""
models.py

This file comtains a reflection of the database schema.
The classes are linked to tables in the database with the sqlalchemy Declarative API.

If a change to this schema is made, it is important to follow these steps to perform a migration of the database:
1. Run the command, replacing <name> with a short description of the upgrade: python make_migration.py "<name>"
2. Run the command: python manage.py upgrade

Note:
Only use single line comments in this file for generate_pymodels.py to work correctly
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import *
Base = declarative_base()


class Highlight(Base):
    __tablename__ = 'highlights'

    ID = Column(Integer, primary_key=True)
    selection = Column(String)
    content = Column(String)
    tags = Column(String)
    url = Column(String)
    date = Column(String)

class Document(Base):
    __tablename__ = 'documents'

    ID = Column(Integer, primary_key=True)
    text = Column(String)

class Term(Base):
    __tablename__ = 'terms'

    ID = Column(Integer, primary_key=True)
    text = Column(String)

class TFIDF(Base):
    __tablename__ = 'tfidf'

    ID = Column(Integer, primary_key=True)

    document_id = Column(Integer, ForeignKey("documents.ID"))
    document = relationship(Document, primaryjoin=document_id == Document.ID)

    term_id = Column(Integer, ForeignKey("terms.ID"))
    term = relationship(Term, primaryjoin=term_id == Term.ID)

    tfidf_value = Column(Float)

metadata = Base.metadata
