# -*- coding: utf-8 -*-
# Author: Nguyen Hoai Nam
from flask import Flask
from flask import request
from flask import make_response
from flask import logging
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.errorhandler(400)
def bad_request(err):
    """
    HTTP 400 code
    """
    logger.error('Invalid request: {} {}.'.format(request.method, request.path))
    return make_response('Bad Request', 400)


@app.errorhandler(404)
def not_found(err):
    """
    HTTP 404 code
    """
    logger.error('File not found: {}'.format(request.path))
    return make_response('Not Found', 404)


@app.errorhandler(500)
def internal_error(err):
    """
    HTTP 500 code
    """
    return make_response('Something went wrong. Sorry for this inconvenience', 500)
