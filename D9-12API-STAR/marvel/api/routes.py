from flask import Blueprint
from auth import get_api_endpoint
import apistar

api = Blueprint('api', __name__)

@api.route('/comics')
def comics():
    return '<h1>Comics:</h1>'


