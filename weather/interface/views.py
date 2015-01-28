# -*- coding: utf-8 -*-
__author__ = 'florije'

from ..basic_handler import BaseHandler
from flask import current_app
from flask.ext.restful import reqparse
from ..config import config
import simplejson
from ..utility import http_client


class HelloHandler(BaseHandler):
    """
    demo
    """

    def get(self):
        return 'hello, world!'


class ProvinceHandler(BaseHandler):
    """
    获取所有的省份的信息。
    """

    def get(self):
        province_url = current_app.config.get('PROVINCE_URL')  # config['development'].PROVINCE_URL
        content = http_client.get_json(province_url)

        return self.json_output(data=simplejson.loads(content))


class DistictHandler(BaseHandler):
    """
    获取省下分的所有区域
    """

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('province_id', type=unicode, required=True, help="province_id cannot be blank!",
                            location='args')
        args = parser.parse_args()

        district_url = current_app.config.get('DISTRICT_URL') % args.province_id  # config['development'].PROVINCE_URL
        content = http_client.get_json(district_url)

        return self.json_output(data=simplejson.loads(content))