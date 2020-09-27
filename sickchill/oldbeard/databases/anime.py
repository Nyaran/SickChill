from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sickchill.oldbeard.databases.abstracts import AbstractContainer

Base = declarative_base(cls=AbstractContainer)
Session = sessionmaker()


class Anime(Base):
    indexer_id = Column(String)
    indexer = Column(Integer)
    network = Column(String)
    genre = Column(Text)
    runtime = Column(Integer)
    quality = Column(Integer)
    airs = Column(Text)
    status = Column(Text)
    flatten_folders = Column(Integer)
    paused = Column(Integer)
    startyear = Column(Integer)
    lang = Column(String)
    subtitles = Column(Integer)
    scene = Column(Integer)
    absolute = Column(Integer)
    default_ep_status = Column(Integer)
    default_ep_status = Column(Integer)
    default_ep_status = Column(Integer)
