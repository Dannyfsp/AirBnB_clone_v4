#!/usr/bin/python3
'''Initializing an app instance using Flask'''

from flask import Flask, Blueprint, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views, url_prefix="/api/v1")
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_storage(exception):
    '''Closing the database storage'''
    storage.close()


@app.errorhandler(404)
def notFound(error):
    '''Returns page not found error message'''
    e = {
        "error": "Not Found"
    }
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if not HBNB_API_PORT else HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)
