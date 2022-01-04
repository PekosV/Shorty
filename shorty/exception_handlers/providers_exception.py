from shorty.exception_handlers.shorty_exception_handler import ShortyExceptionHandler


class ProvidersException(ShortyExceptionHandler):
    def __init__(self,  message):
        self.status = 503
        self.message = message
        super().__init__(self.status, self.message)
