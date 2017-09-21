# -*- coding:utf-8 -*-

import jieba
import jieba.analyse
from app import api, mongo
from flask import jsonify
from flask_restful import Resource
from datetime import datetime
import time

class KEYWORDS(Resource):
    def get(self, date):
        sdate = datetime.strptime(date,'%Y-%m-%d')
        result = mongo.db.news.find({'date':sdate},{'content':1,'_id':0},batch_size=10000)
        contents = [data['content'].replace('\u3000', '') for data in result]
        tags = []
        for content in contents:
            tag = jieba.analyse.extract_tags(content,topK=5,withWeight=True,allowPOS=())
            tags.extend(tag)
        res = [{'WORD':x[0],'WEIGHT':x[1]} for x in tags]
        return jsonify(res)
        
api.add_resource(KEYWORDS, '/api/newscrawl/<date>')
