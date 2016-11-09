class AccessRequest():
    def __init__(self, method, uri):
        self._method = method
        self._uri = uri

    def get_method(self):
        return self._method

    def get_uri(self):
        return self._uri
