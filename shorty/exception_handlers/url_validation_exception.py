from shorty.exception_handlers.shorty_exception_handler import ShortyExceptionHandler


class UrlValidationException(ShortyExceptionHandler):
    def __init__(self, error_response):
        self.message_response = error_response
        self.status = 422
        super().__init__(self.status, self.message_response)
