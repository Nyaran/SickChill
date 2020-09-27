from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr


class AbstractTable(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class AbstractContainer(AbstractTable):
    """
    To store info about items that have items inside.

    Eg: Shows, Anime Shows, Music...
    """
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)


class AbstractItem(AbstractTable):
    """
    To store info about single items

    Eg: Episodes, Movies, Songs...
    """
