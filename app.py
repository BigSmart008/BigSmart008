import os

from flask import request, Flask
from models import *
import re
from exts import *
from views import *
app = Flask(__name__)

db_url = 'sqlite:///' + os.path.join(app.root_path, 'files.db')
print('db_url:',db_url)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象跟踪修改

init_exts(app)
app.register_blueprint(blueprint=blue)

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    BookModel.init_db()



book_view = BookApi.as_view('book_api') #as_view 的参数是用来 给url_for 调用的

app.add_url_rule('/book/',defaults={'book_id':None},view_func=book_view,methods=['GET','POST'])
app.add_url_rule('/',defaults={'book_id':None},view_func=book_view)
app.add_url_rule('/book/<int:book_id>',view_func=book_view,methods=['GET','POST','PUT'])


if __name__ == '__main__':
    app.run(debug=True)



