import os
from flask import Flask

_basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
application.config.from_object('SynAlchemy.settings.local')

from SynAlchemy.database import init_db
init_db()

from SynAlchemy.modules.mod_api.views import api_blueprint
application.register_blueprint(api_blueprint, url_prefix='/api')
