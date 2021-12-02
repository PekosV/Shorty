import pytest

from shorty.exception_handlers.providers_exception import ProvidersException
from shorty.input_verification.provider_verification import ProviderVerification


class TestProvidersVerification:

    def test_provider_validator_bitly(self):
        provider = 'bitly'
        validation = ProviderVerification.is_valid_provider(provider)
        assert validation

    def test_provider_validator_tinyurl(self):
        provider = 'tinyurl'
        validation = ProviderVerification.is_valid_provider(provider)
        assert validation

    def test_provider_validator_tinyurl_different_format(self):
        provider = 'tinyUrl'
        validation = ProviderVerification.is_valid_provider(provider)
        assert validation

    def test_provider_validator_bitly_different_format(self):
        provider = 'BitLy'
        validation = ProviderVerification.is_valid_provider(provider)
        assert validation

    def test_provider_validator_invalid_provider(self):
        provider = 'random provider'
        with pytest.raises(ProvidersException):
            ProviderVerification.validate_provider(provider)
