import re 
import logging
from client2 import LyricsClient

ACCESS_TOKEN = 'h5hOb45eWlZpAmf53hw3HS5fLWFIeT6Gkf0O5I-xV1CGvH8lXN6LF_UFXU11_Ihy'

def main(artist, max_songs):
    """Main function."""
    log_object = logging.getLogger(__name__)
    log_object.setLevel(logging.DEBUG)
    
    client = LyricsClient(ACCESS_TOKEN)
    artist_songs = client._artist_request_songs(artist, max_songs)
    words_songs = [re.sub("[\(\[].*?[\)\]]", "", client._search_artist_song_lyrics(artist_songs['artist'] , song).replace('\n',' ')).split() for song in artist_songs['songs']]
    average = sum(len(word) for word in words_songs)/len(words_songs)
    return average

if __name__ == '__main__':
    artist='Andy Shauf'
    max_songs=100
    print(main(artist, max_songs))


