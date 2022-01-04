from shorty.exception_handlers.url_validation_exception import UrlValidationException
from shorty.providers.provider_retriever import ProviderRetriever
from shorty.input_verification.provider_verification import ProviderVerification
from shorty.input_verification.url_verification import UrlValidator

DEFAULT_PROVIDER = 'bitly'


class ShortyExecution:
    def __init__(self, request):

        self.provider = request.get("provider", DEFAULT_PROVIDER)
        if 'url' not in request:
            raise UrlValidationException("We did not receive a URL, please try again")
        self.url = request['url']
        self.short_link = ""

    def validate_requested_url(self):
        UrlValidator.validate_url(self.url)

    def validate_requested_provider(self):
        ProviderVerification.validate_provider(self.provider)

    def validate_request(self):
        self.validate_requested_url()
        self.validate_requested_provider()

    def shorten_url(self):
        self.validate_request()
        selected_provider = ProviderRetriever.retrieve_provider(self.provider)
        self.short_link = selected_provider.shorten_url(self.url)
        return {"data": {"short_link": self.short_link, "url": self.url}}
