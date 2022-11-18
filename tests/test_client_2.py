import json
from unittest import mock
import pytest
from src.client2 import LyricsClient
import lyricsgenius

@pytest.fixture
def params():
    params = {}
    params['token'] = 'foo'
    yield params

def test_client_raises_unknown_api_when_wrong_api():
    """
    Raises uknown API when no Token is parsed
    """
    with pytest.raises(TypeError) as noAccessToken:
        lyricsclient = LyricsClient(None)
    assert noAccessToken.value.args == ('Invalid token',)

# Patch object works by importing the module in directly here I am patching the class and method search artist
# Can be done with a decorator to looks a little neater
@mock.patch.object(lyricsgenius.Genius, 'search_artist')
def test_client_returns_artist_song(mock):
    """
    returns expected api call
    """
    ACCESS_TOKEN = 'FOO'
    MOCK_ARTIST = 'FOO'
    MOCK_MAX_SONGS = 0
    
    test_client = LyricsClient(ACCESS_TOKEN)
    test_client._genius.search_artist.return_value.songs = [] 
    test_client._genius.search_artist.return_value.name = 'foo'
    test_client._genius.search_artist.return_value.api_path = 'foo'
    
    resp = test_client._artist_request_songs(MOCK_ARTIST, MOCK_MAX_SONGS)
    assert resp == {'songs' : [], 'artist': 'foo'}

@mock.patch.object(lyricsgenius.Genius, 'search_song')
def test_client_returns_artist_lyrics_song(mock):
    """
    returns expected api call
    """
    ACCESS_TOKEN = 'FOO'
    MOCK_ARTIST = 'FOO'
    MOCK_SONG_TITLE = 'MOCKSONG'

    test_client = LyricsClient(ACCESS_TOKEN)
    test_client._genius.search_song.return_value.lyrics = 'foo' 
    
    resp = test_client._search_artist_song_lyrics(MOCK_ARTIST, MOCK_SONG_TITLE)
    assert resp == 'foo'

def test_client_raises_positional_arg_song():
    """
    returns expected api call
    """
    ACCESS_TOKEN = 'FOO'
    MOCK_SONG_TITLE = 'MOCKSONG'

    test_client = LyricsClient(ACCESS_TOKEN)
    with pytest.raises(TypeError) as noAccessToken:
        test_client._search_artist_song_lyrics(MOCK_SONG_TITLE)
    assert noAccessToken.value.args == ("LyricsClient._search_artist_song_lyrics() missing 1 required positional argument: 'song'",)