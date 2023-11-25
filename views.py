import re

from flask import Blueprint, request, jsonify
from flask.views import MethodView
from models import *

class UserApi(MethodView):
    def get(self):
        users = UserModel.query.all()
        res = []
        for user in users:
            res.append({
                'id':user.id,
                'text':user.text,
                'img':user.img
            })

        obj = {
            'status':200,
            'msg':'用户数据获取成功',
            'data':res

        }
        return obj


    def post(self):
        user = UserModel()
        user.text =request.json.get('text')
        user.img = request.json.get('img')
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'status':'success',
            'msg':'数据添加成功'
        })

