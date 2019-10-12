from hashlib import md5  # needed for API auth
from time import time
import os


# get from marvel developer account:
PUBLIC_KEY = os.environ['PUBLIC_KEY']
PRIVATE_KEY = os.environ['PRIVATE_KEY']

def get_api_endpoint(endpoint):
    """generate valid endpoint url based on
    https://developer.marvel.com/documentation"""

    time_stamp = round(time())
    hash_data = f'{time_stamp}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8')
    hash_ = md5(hash_data).hexdigest()
    return f'https://gateway.marvel.com:443/v1/public/' \
           f'{endpoint}?ts={time_stamp}' \
           f'&apikey={PUBLIC_KEY}&hash={hash_}'
