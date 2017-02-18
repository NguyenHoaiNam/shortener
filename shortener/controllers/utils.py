# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from random import SystemRandom as SR

import string
import logging
import config

logger = logging.getLogger(__name__)


def rand():
    """
    Generate random string to be url path
    """
    return ''.join(SR().choice(string.ascii_letters + string.digits)
                   for _ in range(config.RAND_DIR_LENGTH))
