# -*- coding: utf-8 -*-
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from .extensions import mongo, resource, perms, oauth2
from exceptions import api_error_handler

# Import API module
import api.agent
import api.minion

# Config
from . import DEFAULT_CONFIG_CLASS, DEFAULT_APPLICATION_CONFIG_FILE, DEFAULT_GLOBAL_CONFIG_FILE, load_module


def create_app(config=None):
    """Creates the app."""
    # Initialize the app
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def configure_app(app, filename=DEFAULT_GLOBAL_CONFIG_FILE, config_class=DEFAULT_CONFIG_CLASS):
    """
    Configure a Flask app
    :param app:
    :param filename:
    :return:
    """
    # Select config file
    if not os.path.isfile(filename):
        filename = DEFAULT_APPLICATION_CONFIG_FILE

    # Load proper config for app
    config = load_module(filename)
    app.config.from_object(getattr(config, config_class))

    # Correct LOG_FOLDER config
    app.config['LOG_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'logs')
    config.make_dir(app.config['LOG_FOLDER'])

    # Config Flask components
    configure_extensions(app)
    configure_blueprints(app)
    configure_log_handlers(app)
    configure_error_handlers(app)


def configure_extensions(app):
    """
    :param app: flask app (main app)
    :return:
    """
    mongo.init_app(app)
    perms.init_app(app)
    resource.init_app(app)
    oauth2.init_app(app)


def configure_blueprints(app):
    """
    Hàm khai báo các URL prefix.
    :param app: Đối tượng flask app.
    :return:
    """
    app.register_blueprint(api.agent.api)
    app.register_blueprint(api.minion.api)


def configure_log_handlers(app):
    """
    Config log
    :param app: flask app
    :return: not return
    """
    fmt = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    formatter = logging.Formatter(fmt)

    info_log = os.path.join(app.config['LOG_FOLDER'], app.config['INFO_LOG'])
    info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.DEBUG)
    info_file_handler.setFormatter(formatter)
    app.logger.addHandler(info_file_handler)

    error_log = os.path.join(app.config['LOG_FOLDER'], app.config['ERROR_LOG'])
    error_file_handler = logging.handlers.RotatingFileHandler(error_log, maxBytes=100000, backupCount=10)
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

    handler_console = logging.StreamHandler(stream=sys.stdout)
    handler_console.setFormatter(formatter)
    handler_console.setLevel(logging.INFO)
    app.logger.addHandler(handler_console)

    # set proper log level
    app.logger.setLevel(logging.DEBUG if app.debug else logging.ERROR)

    # unify log format for all handers
    for h in app.logger.handlers:
        h.setFormatter(formatter)

    app.logger.info('Config filename: {0}'.format(app.config['FILENAME']))
    app.logger.info('App log folder: {0}'.format(app.config['LOG_FOLDER']))


def configure_error_handlers(app):
    """Configures the error handlers."""

    for exception in default_exceptions:
        app.register_error_handler(exception, api_error_handler)
    app.register_error_handler(Exception, api_error_handler)