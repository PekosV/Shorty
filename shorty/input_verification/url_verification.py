import validators

from shorty.exception_handlers.url_validation_exception import UrlValidationException


class UrlValidator:

    @classmethod
    def validate_url(cls, url):
        if not url:
            raise UrlValidationException("Empty URL field")
        if not cls._is_valid_url(url):
            raise UrlValidationException("Malformed URL")

    @classmethod
    def _is_valid_url(cls, url):
        return validators.url(url)
