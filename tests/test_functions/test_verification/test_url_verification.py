import pytest

from shorty.exception_handlers.url_validation_exception import UrlValidationException
from shorty.input_verification.url_verification import UrlValidator


class TestUrlVerification:

    def test_url_validation_valid_url(self):
        valid_url = "https://withplum.com"
        validation = UrlValidator._is_valid_url(valid_url)
        assert validation

    def test_url_validation_invalid_url(self):
        invalid_url = "https://with plum.com"
        validation = UrlValidator._is_valid_url(invalid_url)
        assert not validation

    def test_url_validation_invalid_url_exception(self):
        invalid_url = "https://with plum.com"
        with pytest.raises(UrlValidationException):
            UrlValidator.validate_url(invalid_url)
