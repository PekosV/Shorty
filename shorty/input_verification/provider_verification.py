from shorty.exception_handlers.providers_exception import ProvidersException


class ProviderVerification:
    
    @classmethod
    def validate_provider(cls, provider):
        if not cls.is_valid_provider(provider):
            raise ProvidersException("You entered an  invalid provider")

    @classmethod
    def is_valid_provider(cls, provider):
        return provider.lower() in ["bitly", "tinyurl"]
