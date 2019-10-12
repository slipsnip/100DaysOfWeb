from flask import Flask

app = Flask(__name__)

from marvel.api.routes import api
from marvel.site.routes import site

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(site)

