# -*- coding:utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 跨域访问
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False)) # 返回中文
app.config.from_object('config')
api = Api(app)
mongo = PyMongo(app, config_prefix='MONGO')

from app import views
