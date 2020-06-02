
class KeyNotFoundException(Exception):
    def __init__(self, name: str , code : int):
        self.name = name
        self.error_code = code

class InternalServerException(Exception):
    def __init__(self, name: str , code : int):
        self.name = name
        self.error_code = code