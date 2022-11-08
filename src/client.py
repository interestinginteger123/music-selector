import json
import logging
import lyricsgenius

ARTIST_SONGS = '/ox/3.0'
ARTIST_LIBRARY = '/ox/4.0'
API_PATH_SSO = '/api'
API_PATHS = (ARTIST_SONGS, ARTIST_LIBRARY )

class RequestError(ValueError):
    """Exception for bad request response"""
    pass

class UnknownAPIFormatError(ValueError):
    """Client has unknown format error."""
    pass

class NoJsonError(ValueError):
    """Client has no JSON payload."""
    pass

class Client(object):
    """
    Client for making requests for Song Artists
    """
    def __init__(self, url, access_token, api_path):
        self.logger = logging.getLogger(__name__)
        self.url = url
        self.access_token = access_token
        self.api_path = api_path

        if api_path not in API_PATHS:
            msg = '"{}" is not a recognized API path.'.format(api_path)
            raise UnknownAPIFormatError(msg)
        self._session = requests.Session()
        self.logger = logging.getLogger()

    def log_request(self, response):
        try:
            self.logger.debug(json.loads(response.text))
        except ValueError:
            self.logger.debug("%s" % response.text)
        self.logger.debug('{0:=<45}'.format('api call finished'))
    
    def _request(self, json=None, headers=None, retry=False, method='GET'):
        """API client to request data."""

        if headers is None:
            headers = {}
        
        if json:
            response = self._session.request(method, self.url, headers=headers,
                                             json=json, auth=self.access_token)
        else:
            msg = '"{}" is no JSON payload to select from'
            raise NoJsonError(msg)
        self.log_request(response)
        
        if retry or response.status_code == requests.codes.ok:
            return response
        
        else:
            raise RequestError(response)

        








