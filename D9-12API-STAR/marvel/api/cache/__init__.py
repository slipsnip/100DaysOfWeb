import os
import json
from pathlib import Path


# https://developer.marvel.com/docs
MARVEL_OBJECTS = 'characters comics creators events series stories'.split()
CACHE_DIR = os.environ['CACHE_DIR']


def get_cache_marvel_data(endpoint):
    """Helper function to cache Marvel API JSON data to file"""

    data = json.dumps({})
    cache_filename = Path(CACHE_DIR, f'cache_{endpoint}')
    if cache_filename.exists():
        with open(cache_filename) as cache_file:
            data = cache_file.read()
        return json.loads(data)

    return data
