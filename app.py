import os
from flask import Flask
import flask_login

_basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
application.config.from_object('app.settings.local')
application.config['MAX_CONTENT_PATH'] = 50000

from app.database import init_db
init_db()

from app.modules.mod_user.views import main_blueprint
application.register_blueprint(main_blueprint, url_prefix='/user')