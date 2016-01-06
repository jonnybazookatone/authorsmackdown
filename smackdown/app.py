# encoding: utf-8
"""
Application factory
"""

import logging.config
from views import SmackView, IndexView
from flask import Flask
from flask.ext.cors import CORS
from flask.ext.restful import Api

def create_app():
    """
    Create the application and return it to the user

    :return: flask.Flask application
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Load config and logging
    load_config(app)
    logging.config.dictConfig(
        app.config['SMACKDOWN_LOGGING']
    )

    # Cache
    # cache.init_app(app, config=app.config['CACHE'])

    # CORS
    CORS(
        app,
        resource={
            r'/status': {'origins': app.config['CORS_ORIGINS']}
        }
    )
    # Register extensions
    api = Api(app)

    # Add end points
    api.add_resource(IndexView, '/', methods=['GET'])
    api.add_resource(SmackView, '/smackdown', methods=['POST'])

    return app


def load_config(app):
    """
    Loads configuration in the following order:
        1. config.py
        2. local_config.py (ignore failures)
        3. consul (ignore failures)
    :param app: flask.Flask application instance
    :return: None
    """

    app.config.from_pyfile('config.py')

    try:
        app.config.from_pyfile('local_config.py')
    except IOError:
        app.logger.warning('Could not load local_config.py')


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=False)
