import re

from flask import Blueprint, request, jsonify
from flask.views import MethodView
from models import *
blue = Blueprint('user',__name__)

class BookApi(MethodView):
    def get(self,book_id):
        # 获取参数

        if book_id:
            return '成功获取到'+str(book_id)+'的详细信息'
        else:
            return '成功获取到所有的书籍'
    def post(self,book_id):
        book = BookModel()
        book.text =request.json.get('text')
        book.img = request.json.get('img')
        db.session.add(book)
        db.session.commit()
        return jsonify({
            'status':'success',
            'msg':'数据添加成功'
        })

    def put(self,book_id):
        book = BookModel.query.get(book_id)
        book.text = request.json.get('text')
        book.img = request.json.get('text')
        db.session.commit()
        return jsonify({
            'status': 'success',
            'msg': '数据修改成功'
        })
        #请求参数


    def delete(self,book_id):
        db.session.delete(book_id)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'msg': '数据删除成功'
        })


#还可以添加default 还可以添加mathod