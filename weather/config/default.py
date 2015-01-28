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

    PROVINCE_URL = 'http://www.weather.com.cn/data/city3jdata/china.html'  # 获取省份
    DISTRICT_URL = 'http://weather.com.cn/data/city3jdata/provshi/%s.html'  # 获取区域
    CITY_URL = 'http://weather.com.cn/data/city3jdata/station/%s%s.html'  # 获取城市

    CURRENT_DAY_URL = 'http://weather.com.cn/data/cityinfo/%s%s%s.html'  # 获取当天天气信息
    CURRENT_TIME_URL = 'http://weather.com.cn/data/sk/%s%s%s.html'  # 获取实时天气信息

    MUNICIPALITIES = ['10101', '10102', '10103', '10104']

    @staticmethod
    def init_app(app):
        pass