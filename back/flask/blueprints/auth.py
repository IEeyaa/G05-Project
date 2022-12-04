# 和用户信息有关的蓝图页
# About LoginView.vue and RegisterView.vue
import re

from flask import Blueprint, request, jsonify, make_response
from util import Result
from models import User
from exts import db

bp = Blueprint("auth", __name__, url_prefix="/")


# POST:将前端的数据提交给服务器
@bp.route("login", methods=["POST"])
def login_view():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    username = data.get('username', None)
    password = data.get('password', None)
    query = db.session.query(User).filter(User.user_name == username).first()
    for i in query:
        password_in = i[2]
    if password == password_in:
        pass
    # 登录页面未完成
@bp.route("register", methods=["POST"])
def register_view():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    message = {}
    username = data.get('rName', None)
    password = data.get('rPassword', None)
    email = data.get('rEmail', None)

    # 判断是否为空
    if 'username' not in data or not username:
        message['username'] = "请提供一个有效的用户名！"
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,' \
              '3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$ '
    if 'email' not in data or not re.match(pattern, email):
        message['email'] = "请提供一个有效的邮箱地址！"
    if 'password' not in data or not password:
        message['password'] = "请提供一个有效的密码！"

    # 检查数据库中是否有该用户
    if User.query.filter_by(User.user_name == username).first():
        message['username'] = '用户名已存在'
    if User.query.filter_by(User.email == email).first():
        message['email'] = '邮箱已存在'
    if message:
        return Result.error(400, message)

    # 创建新用户
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    return Result.success(user.user_id)
