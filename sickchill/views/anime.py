import logging

from sickchill import settings
from sickchill.oldbeard import config

from .common import PageTemplate
from .index import WebRoot

logger = logging.getLogger('sickchill.anime')


class AnimeHandler(WebRoot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _genericMessage(self, subject=None, message=None):
        t = PageTemplate(rh=self, filename="genericMessage.mako")
        return t.render(message=message, subject=subject, topmenu="anime", title="")

    def index(self):
        t = PageTemplate(rh=self, filename="anime/index.mako")
        return t.render(title=_("Anime"), header=_("Anime List"), topmenu="anime", anime=settings.anime_list, controller="anime", action="index")

    def search(self):
        query = self.get_body_argument('query', '')
        adult = config.checkbox_to_value(self.get_body_argument('adult', False))
        search_results = []
        if query:
            search_results = settings.anime_list.search_anidb(query=query, adult=adult)
        t = PageTemplate(rh=self, filename="anime/search.mako")
        return t.render(title=_("Anime"), header=_("Anime Search"), topmenu="animes", controller="anime", action="search",
                        search_results=search_results, animes=settings.anime_list, query=query, adult=adult)

    def add(self):
        pass

    def remove(self):
        pass

    def details(self):
        pass
