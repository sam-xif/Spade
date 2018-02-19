from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
documents = Table('documents', post_meta,
    Column('ID', Integer, primary_key=True, nullable=False),
    Column('text', String),
)

terms = Table('terms', post_meta,
    Column('ID', Integer, primary_key=True, nullable=False),
    Column('text', String),
)

tfidf = Table('tfidf', post_meta,
    Column('ID', Integer, primary_key=True, nullable=False),
    Column('document_id', Integer),
    Column('term_id', Integer),
    Column('tfidf_value', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['documents'].create()
    post_meta.tables['terms'].create()
    post_meta.tables['tfidf'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['documents'].drop()
    post_meta.tables['terms'].drop()
    post_meta.tables['tfidf'].drop()

