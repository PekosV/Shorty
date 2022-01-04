from abc import abstractmethod


class Provider:
    @classmethod
    @abstractmethod
    def shorten_url(cls, url):
        pass
