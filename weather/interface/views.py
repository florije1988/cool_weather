# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import current_app
from flask.ext.restful import reqparse

from ..utility import http_client
from ..basic_handler import BaseHandler
from ..config import config

import simplejson


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


class DistrictHandler(BaseHandler):
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


class CityHandler(BaseHandler):
    """
    获取城市详细列表
    """

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('province_id', type=unicode, required=True, help="province_id cannot be blank!",
                            location='args')
        parser.add_argument('district_id', type=unicode, required=True, help="district_id cannot be blank!",
                            location='args')
        args = parser.parse_args()

        city_url = current_app.config.get('CITY_URL') % (args.province_id, args.district_id,)
        content = http_client.get_json(city_url)

        return self.json_output(data=simplejson.loads(content))


class LocationDayHandler(BaseHandler):
    """
    获取某地的当天的天气
    """

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('province_id', type=unicode, required=True, help="province_id cannot be blank!",
                            location='args')
        parser.add_argument('district_id', type=unicode, required=True, help="district_id cannot be blank!",
                            location='args')
        parser.add_argument('city_id', type=unicode, required=True, help="city_id cannot be blank!", location='args')
        args = parser.parse_args()

        if args.province_id in current_app.config.get('MUNICIPALITIES'):
            city_url = current_app.config.get('CURRENT_DAY_URL') % (args.province_id, args.city_id, args.district_id)
        else:
            city_url = current_app.config.get('CURRENT_DAY_URL') % (args.province_id, args.district_id, args.city_id)
        content = http_client.get_json(city_url)

        return self.json_output(data=simplejson.loads(content))


class LocationTimeHandler(BaseHandler):
    """
    获取某地的当时的天气
    """

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('province_id', type=unicode, required=True, help="province_id cannot be blank!",
                            location='args')
        parser.add_argument('district_id', type=unicode, required=True, help="district_id cannot be blank!",
                            location='args')
        parser.add_argument('city_id', type=unicode, required=True, help="city_id cannot be blank!", location='args')
        args = parser.parse_args()

        if args.province_id in current_app.config.get('MUNICIPALITIES'):
            city_url = current_app.config.get('CURRENT_TIME_URL') % (args.province_id, args.city_id, args.district_id)
        else:
            city_url = current_app.config.get('CURRENT_TIME_URL') % (args.province_id, args.district_id, args.city_id)
        content = http_client.get_json(city_url)

        return self.json_output(data=simplejson.loads(content))