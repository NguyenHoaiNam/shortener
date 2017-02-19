# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from random import SystemRandom as SR
from shortener.model import models

import string
import logging
import config
import socket

logger = logging.getLogger(__name__)

PROTOCOL = 'http://'
PORT = config.server['port']


def rand():
    """
    Generate random string to be url path
    """
    return ''.join(SR().choice(string.ascii_letters + string.digits)
                   for _ in range(config.RAND_DIR_LENGTH))


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_short_url(short_url):
    host_ip = config.server['host']
    if host_ip == '0.0.0.0':
        host_ip = get_ip()
    search_name = 'link'
    url = PROTOCOL + host_ip + ':' + PORT + '/' + search_name + '/' + short_url
    return url


def get_org_link_by_short_link(session, short_link):
    for link in session.query(models.Url).filter_by(short_link=short_link):
        origin_link = link.org_link
    return origin_link