import os
from flask import Flask, jsonify

_basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
application.config.from_object('SynAlchemy.settings.local')

from SynAlchemy.database import init_db
init_db()

from SynAlchemy.modules.mod_api.views import api_blueprint
application.register_blueprint(api_blueprint, url_prefix='/api')

@application.errorhandler(404)
def page_not_found(e):
	return jsonify({"error" : "Error 404 Not Found"})
