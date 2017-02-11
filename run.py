#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from shortener.handlers import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--port', type=int, default=3007,
                        help='Listen port. Default: "3007"')
    parser.add_argument('-i', '--ip', default='0.0.0.0',
                        help='Listen IP. Default: "0.0.0.0"')
    parser.add_argument('-d', '--debug', default=None, action='store_true',
                        help='Enable debug mode')
    args = parser.parse_args()

    app.run(host=args.ip, port=args.port, debug=args.debug)
