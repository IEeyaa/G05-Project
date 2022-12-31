from exts import db
from sqlalchemy import ForeignKey


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(30), nullable=True)
    motto = db.Column(db.String(150), nullable=True)

    def to_dict(self):
        """
        封装 User 对象，传递给前端只能是 json 格式，不能是实例对象
        :param include_email: 只有当用户请求自己数据时，才包含 email
        :return
        """
        data = {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'password': self.password,
            'email': self.email,
            'city': self.city,
            'motto': self.motto
        }
        return data

    def from_dict(self, data, new_user=False):
        """
        将前端发送过来的 json 对象转换为 User 对象
        :param data:
        :param new_user:
        :return:
        """

        for field in ['user_name', 'email']:
            if field in data:
                setattr(self, field, data[field])
            if new_user and 'password' in data:
                self.password = data['password']


class Thesis(db.Model):
    __tablename__ = "thesis"
    __table_args__ = {'extend_existing': True}
    thesis_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    publication_date = db.Column(db.Date)
    image_link = db.Column(db.String(150), nullable=False)
    abstract = db.Column(db.String(2500), nullable=False)
    link = db.Column(db.String(150))
    citation_num = db.Column(db.Integer)
    rating = db.Column(db.Float)

    def to_dict(self):
        data = {
            'thesis_id': self.thesis_id,
            'title': self.title,
            'author': self.author,
            'publication_date': self.publication_date,
            'image_link': self.image_link,
            'abstract': self.abstract,
            'link': self.link,
            'citation_num': self.citation_num,
            'rating': self.rating
        }
        return data


class Favorites(db.Model):
    __tablename__ = "favorites"
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False, primary_key=True)
    thesis_id = db.Column(db.Integer, ForeignKey('thesis.thesis_id'), nullable=False, primary_key=True)


class Keyword(db.Model):
    __tablenam__ = "keyword"
    __table_args__ = {'extend_existing': True}
    data = db.Column(db.String(20), nullable=False, primary_key=True)
    value = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        data = {
            'data': self.data,
            'value': self.value
        }
        return data
