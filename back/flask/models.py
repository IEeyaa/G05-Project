# 存储数据库模型
from exts import db
from sqlalchemy import ForeignKey

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)

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