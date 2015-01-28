# -*- coding: utf-8 -*-
__author__ = 'florije'

from ..basic_handler import BaseHandler


class HelloHandler(BaseHandler):
    """
    demo
    """
    def get(self):
        return 'hello, world'