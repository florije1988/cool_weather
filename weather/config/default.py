# -*- coding: utf-8 -*-
__author__ = 'boqingfu'


class Config:
    def __init__(self):
        pass

    DEBUG = False
    TESTING = False

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    APP_DEBUG = True
    HOST = 'localhost'
    PORT = 5000
    LOG_PATH = 'logs'
    LOG_NAME = 'proj_logs.log'

    province_url = 'http://www.weather.com.cn/data/city3jdata/china.html'  # 获取省份
    district_url = 'http://weather.com.cn/data/city3jdata/provshi/%s.html'  # 获取区域
    city_url = 'http://weather.com.cn/data/city3jdata/station/%s%s.html'  # 获取城市

    current_day = 'http://weather.com.cn/data/cityinfo/%s%s%s.html'  # 获取当天天气信息
    current_time = 'http://weather.com.cn/data/sk/%s%s%s.html'  # 获取实时天气信息

    @staticmethod
    def init_app(app):
        pass