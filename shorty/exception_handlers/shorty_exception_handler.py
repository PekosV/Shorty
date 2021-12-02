class ShortyExceptionHandler(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def error_response(self):
        response = {"status_code": self.status_code, "message": self.message}
        return {"error": response}

