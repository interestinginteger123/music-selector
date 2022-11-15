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
            self.logger.debug(json.loads(response.api_path))
        except ValueError:
            self.logger.debug("%s" % response.api_path)
        self.logger.debug('{0:=<45}'.format('lyrics genious call finished'))
    
    def _search_artist_song_lyrics(self, artist_name, song):
        if artist_name:
            response = self._genius.search_song(artist_name, song.title)
            self.log_request(response)
            return response.lyrics
        else:
            msg = 'No artist parsed to request'
            raise NoArtistError(msg)

    def _artist_request_songs(self, artist=None, max_songs=0) -> dict:
        """Call for artist request."""

        if artist:
            response = self._genius.search_artist(artist, max_songs=max_songs, sort="title")
            self.log_request(response)
            return {'songs': response.songs, 'artist': response.name}
        else:
            msg = 'No artist parsed to request'
            raise NoArtistError(msg)
        

        

        








