from typing import Optional

from shorty.providers.bitly import Bitly
from shorty.providers.provider import Provider
from shorty.providers.tinyurl import TinyUrl


class ProviderRetriever:

    providers = {"tinyurl": TinyUrl, "bitly": Bitly}

    @classmethod
    def retrieve_provider(cls, provider_name) -> Optional[Provider]:
        return cls.providers.get(provider_name)

