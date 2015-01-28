# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Blueprint
from ..custom_api import Api

app_interface = Blueprint('app_interface', __name__)
api_interface = Api(app_interface, catch_all_404s=True)

from . import views

api_interface.add_resource(views.HelloHandler, '/')
api_interface.add_resource(views.ProvinceHandler, '/province')
api_interface.add_resource(views.DistrictHandler, '/district')
api_interface.add_resource(views.CityHandler, '/city')
api_interface.add_resource(views.LocationDayHandler, '/day')
api_interface.add_resource(views.LocationTimeHandler, '/time')