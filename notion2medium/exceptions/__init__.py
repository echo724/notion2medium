class ClientTokenException(Exception):
    def __init__(self, client_type: str):
        self._type = client_type

    def __str__(self):
        return f"Cannot get {self._type} token from os environment."
