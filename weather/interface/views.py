# -*- coding: utf-8 -*-
__author__ = 'florije'

from ..basic_handler import BaseHandler
from flask import current_app
import urllib
import urllib2


class HelloHandler(BaseHandler):
    """
    demo
    """

    def get(self):
        url = current_app.config.get('PROVINCE_URL')
        req_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Connection': 'close',
            'Referer': None  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
        }
        req_timeout = 10
        request = urllib2.Request(url, None, req_header)
        response = urllib2.urlopen(request, None, req_timeout)
        html = response.read()
        print(html)

        return html