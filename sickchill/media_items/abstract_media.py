import logging
from abc import ABCMeta, abstractmethod

from sickchill import settings

logger = logging.getLogger('sickchill.abstract_media_item')


class AbstractMediaList(metaclass=ABCMeta):
    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def search_indexer(indexer, query=None, indexer_id=None, year=None, language=None, adult=False):
        pass

    @staticmethod
    @abstractmethod
    def popular_indexer(indexer, language=None):
        pass

    @abstractmethod
    def add_from_tmdb(self, tmdb_id: str, language: str = settings.INDEXER_DEFAULT_LANGUAGE):
        pass

    @abstractmethod
    def add_from_imdb(self, imdb_id: str, language: str = settings.INDEXER_DEFAULT_LANGUAGE, tmdb_primary=False):
        pass

    def commit(self, instance=None):
        logger.debug('Committing')
        if instance:
            self.session.add(instance)
        self.session.flush()
        self.session.commit()

    def delete(self, pk):
        instance = self.query.get(pk)
        if instance:
            self.session.delete(instance)

    @property
    @abstractmethod
    def query(self):
        pass

    def by_slug(self, slug):
        return self.query.filter_by(slug=slug).first()

    @abstractmethod
    def search_providers(self, media_object):
        pass
