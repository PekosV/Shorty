import json

import requests

from shorty.exception_handlers.providers_exception import ProvidersException
from shorty.providers.bitly import Bitly

TOKEN = "ZqsoUZrTWw1T2enGraRb3HHKY7jnAh3bDoCGKU45OP0BrgND6r2Mdk6ADP3y"


class TinyUrl:

    @classmethod
    def shorten_url(cls, url):
        try:
            headers = {
                'Authorization': f'Bearer {TOKEN}',
                'Content-Type': 'application/json',
            }

            data = {"url": url}

            bitly_response = requests.post('https://api.tinyurl.com/create', headers=headers, data=json.dumps(data))

            if bitly_response.status_code == 503:
                raise ProvidersException('TinyUrl seems to be unavailable at the moment. Please try a different '
                                         'provider')
            elif bitly_response.status_code != 200:
                raise ProvidersException("tinyurl")

            return bitly_response.json()["data"]["tiny_url"]

        except Exception:
            raise ProvidersException("tinyurl")
