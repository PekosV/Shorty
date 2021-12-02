import json

import requests

from shorty.exception_handlers.providers_exception import ProvidersException
from shorty.providers.provider import Provider


class Bitly(Provider):

    @classmethod
    def shorten_url(cls, url):
        try:
            headers = {
                'Authorization': 'Bearer 2ef4aa326161a0f6550b4a6e3f93201ce118b899',
                'Content-Type': 'application/json',
            }

            data = {"long_url": url}

            bitly_response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers,
                                           data=json.dumps(data))

            if bitly_response.status_code == 503:

                raise ProvidersException('Bitly seems to be unavailable at the moment. Please try a different provider')

            if bitly_response.status_code not in [200, 201]:

                raise ProvidersException("bitly")

            return bitly_response.json()["link"]

        except Exception:
            raise ProvidersException("bitly")
