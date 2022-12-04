# 存储数据库模型
from exts import db
from sqlalchemy import ForeignKey


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        """
        封装 User 对象，传递给前端只能是 json 格式，不能是实例对象
        :param include_email: 只有当用户请求自己数据时，才包含 email
        :return
        """
        data = {
            'id': self.user_id,
            'username': self.user_name
        }
        return data

    def from_dict(self, data, new_user=False):
        """
        将前端发送过来的 json 对象转换为 User 对象
        :param data:
        :param new_user:
        :return:
        """

        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
            if new_user and 'password' in data:
                self.password = data['password']


class Thesis(db.Model):
    __tablename__ = "thesis"
    thesis_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    publication_date = db.Column(db.Date)
    journal = db.Column(db.String(50), nullable=False)
    abstract = db.Column(db.String(1500), nullable=False)
    link = db.Column(db.String(150))
    citation_num = db.Column(db.Integer)
    rating = db.Column(db.Float)


class Favorites(db.Model):
    __tablename__ = "favorites"
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False, primary_key=True)
    thesis_id = db.Column(db.Integer, ForeignKey('thesis.thesis_id'), nullable=False, primary_key=True)
