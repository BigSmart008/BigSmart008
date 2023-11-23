from exts import *
class BookModel(db.Model):
    __tablename__='file'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    text = db.Column(db.Text)
    img = db.Column(db.Text)

    @staticmethod
    def init_db():
        rets = [
            ('pikaqiu','1.png'),
            ('baolongshou','2.png')
        ]
        for ret in rets:
            file = BookModel()
            file.text = ret[0]
            file.img = ret[1]
            db.session.add(file)

        db.session.commit()


# 本周 完成java 和python