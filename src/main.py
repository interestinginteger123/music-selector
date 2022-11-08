import pandas as pd
import logging
from client import Client

def main(artist):
    """Main function."""

    log_object = logging.getLogger(__name__)
    log_object.setLevel(logging.DEBUG)
    
    artist_songs = artist_songs(log_object,)

    client = Client()

if __name__ == '__main__':
    artist='foo'
    main(artist)

