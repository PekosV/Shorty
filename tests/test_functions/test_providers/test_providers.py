import pytest

from shorty.exception_handlers.providers_exception import ProvidersException
from shorty.providers.bitly import Bitly
from shorty.providers.provider_retriever import ProviderRetriever
from shorty.providers.tinyurl import TinyUrl


class TestProviders:

    def test_bitly_valid_url(self):
        valid_url = "https://withplum.com/"
        response = Bitly.shorten_url(valid_url)
        assert response.startswith("https://bit.ly/")

    def test_tinyurl_valid_url(self):
        valid_url = "https://withplum.com/"
        response = TinyUrl.shorten_url(valid_url)
        assert response.startswith("https://tinyurl.com/")

    def test_provider_retriever_bitly(self):
        requested_provider = "bitly"
        retrieved_provider = ProviderRetriever.retrieve_provider(requested_provider)
        assert retrieved_provider == Bitly

    def test_provider_retriever_tinyurl(self):
        requested_provider = "tinyurl"
        retrieved_provider = ProviderRetriever.retrieve_provider(requested_provider)
        assert retrieved_provider == TinyUrl
