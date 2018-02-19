from sqlalchemy import *
from migrate import *

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
    
metadata = Base.metadata

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    Base.metadata.bind = migrate_engine
    Base.metadata.create_all(migrate_engine)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    Base.metadata.bind = migrate_engine
    Base.metadata.drop_all(migrate_engine)
