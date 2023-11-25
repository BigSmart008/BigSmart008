import os
from flask import request, Flask
from models import *
import re
from exts import *
from views import *
app = Flask(__name__)

db_url = 'sqlite:///' + os.path.join(app.root_path, 'users.db')
print('db_url:',db_url)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象跟踪修改

init_exts(app)

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    UserModel.init_db()


user_view = UserApi.as_view('user_view') #as_view 的参数是用来 给url_for 调用的

app.add_url_rule('/',view_func=user_view,methods=['GET'])
app.add_url_rule('/fileUpload/',view_func=user_view,methods=['POST'])
if __name__ == '__main__':
    app.run(debug=True)



