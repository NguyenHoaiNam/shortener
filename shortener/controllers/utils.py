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
    """
    This function is to get IP which is used to connect Internet
    """
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
    """
    Get origin link from short link
    :param session: this param is session to connect to database
    :param short_link: Short link
    """
    origin_link = session.query(models.Url).filter(models.Url.short_link ==
                                                   short_link).one()
    return origin_link.org_link


def get_short_link_by_org_link(session, org_link):
    short_link = session.query(models.Url).filter(models.Url.org_link ==
                                                  org_link).one()
    return short_link.short_link
