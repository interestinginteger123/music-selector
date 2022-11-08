import json
import logging
import lyricsgenius

class NoArtistError(ValueError):
    """
    Raises when no artist is parsed
    """
    pass

class LyricsClient(object):
    """
    Client for making requests for Song Artists
    """
    def __init__(self, access_token=None):
        self._genius = lyricsgenius.Genius(access_token)
        self.logger = logging.getLogger()

    def log_request(self, response):
        try:
            self.logger.debug(json.loads(response.text))
        except ValueError:
            self.logger.debug("%s" % response.text)
        self.logger.debug('{0:=<45}'.format('lyrics genious call finished'))
    
    def _artist_request(self, artist=None):
        """Call for artist request."""

        if artist:
            response = self._genius.search_artist(artist, max_songs=3)
            self.log_request(response)
            return response
        else:
            msg = 'No artist parsed to request'
            raise NoArtistError(msg)
        

        

        








