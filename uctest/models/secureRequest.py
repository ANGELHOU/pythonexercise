import requests
from ..settings import SERVER, PROTOCOL, USERS, USER
import getCookie


class SecureRequest():
    def __init__(self, requestObj, user=USER, protocol=PROTOCOL, server=SERVER, **kwargs):
        print 'inside SecureRequest'
        self._session, self._headers = getCookie.Cookie(
            USER).session_and_cookie()
        self._uri = requestObj.get_uri()
        self._method = requestObj.get_method()
        self._url = protocol + server + self._uri
        if kwargs:
            self._payload = kwargs
        else:
            self._payload = None
        self._res = self._send_request()

    def _send_request(self):
        if self._method == 'post':
            res = self._session.post(
                self._url, data=self._payload, headers=self._headers)
        elif self._method == 'get':
            res = self._session.get(
                self._url, params=self._payload, headers=self._headers)
        else:
            pass
        return res

    def response(self):
        return self._res
