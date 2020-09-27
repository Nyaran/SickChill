import json
import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sickchill import settings
from sickchill.media_items.abstract_media import AbstractMediaList
from sickchill.oldbeard.databases import anime
from sickchill.oldbeard.db import db_cons, db_full_path, db_locks


class AnimeList(AbstractMediaList):
    def __init__(self):
        # tmdbsimple.API_KEY = settings.TMDB_API_KEY

        self.filename = "anime.db"
        self.full_path = db_full_path(self.filename)

        if self.filename not in db_cons or not db_cons[self.filename]:
            anime.Session.configure(
                bind=create_engine(
                    f"sqlite:///{self.full_path}",
                    echo=True,
                    connect_args={"check_same_thread": False},
                    json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False)
                )
            )
            self.session: Session = anime.Session()
            anime.Base.metadata.create_all(self.session.bind, checkfirst=True)

            db_locks[self.filename] = threading.Lock()
            db_cons[self.filename] = self.session
        else:
            self.session: Session = db_cons[self.filename]

        # self.imdb = imdb.IMDb()
        # try:
        #    self.imdb.topBottomProxy.moviemeter100_parser.rules[0].extractor.rules.append(
        #        Rule(
        #            key='cover url',
        #            extractor=Path('./td[@class="posterColumn"]/a/img/@src')
        #        )
        #    )
        # except:
        #    pass

    def search_indexer(self, indexer, query=None, indexer_id=None, year=None, language=None, adult=False):
        if indexer == 'anidb':
            self.search_anidb(query, language)

    @staticmethod
    def popular_indexer(indexer, language=None):
        pass

    def search_anidb(self, query: str = ''):
        anidb
        pass

    def popular_anidb(self):
        pass

    def add_from_tmdb(self, tmdb_id: str, language: str = settings.INDEXER_DEFAULT_LANGUAGE):
        pass

    def add_from_imdb(self, imdb_id: str, language: str = settings.INDEXER_DEFAULT_LANGUAGE, tmdb_primary=False):
        pass

    @property
    def query(self):
        pass

    def by_slug(self, slug):
        pass

    def search_providers(self, media_object):
        pass

    def snatch_movie(self, result):
        pass

    def search_thread(self):
        pass
