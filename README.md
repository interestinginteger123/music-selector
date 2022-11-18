# Music Selector

Mustic selector is a Python project for finding the average words per artist

## Installation

Use the package manager [poetry](https://python-poetry.org/docs/) to install music-selector.

```bash
poetry shell 
poetry install
```

## Usage

```python
import LyricsClient

# returns 'Artists Songs'
LyricsClient._search_artist_song_lyrics('word', 1)

# returns 'Artists lyrics of song'
LyricsClient._artist_request_songs('goose', 'song')

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)


Using the genius API to leverage and calculate the average songs per 

TODO: API gateway, WAF harnassed to a lambda to do this.
TODO: enhance logging components
TODO: 

Look for linters for the project how are you going to run the project
