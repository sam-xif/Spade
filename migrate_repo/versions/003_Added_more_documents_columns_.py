from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
documents = Table('documents', pre_meta,
    Column('ID', Integer, primary_key=True, nullable=False),
    Column('text', String),
)

documents = Table('documents', post_meta,
    Column('ID', Integer, primary_key=True, nullable=False),
    Column('words', String),
    Column('tags', String),
    Column('raw', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['documents'].columns['text'].drop()
    post_meta.tables['documents'].columns['raw'].create()
    post_meta.tables['documents'].columns['tags'].create()
    post_meta.tables['documents'].columns['words'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['documents'].columns['text'].create()
    post_meta.tables['documents'].columns['raw'].drop()
    post_meta.tables['documents'].columns['tags'].drop()
    post_meta.tables['documents'].columns['words'].drop()

