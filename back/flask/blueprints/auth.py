# 和用户信息有关的蓝图页
# About LoginView.vue and RegisterView.vue
import re

from flask import Blueprint, request, jsonify, make_response
from util import Result
from models import User
from exts import db

bp = Blueprint("auth", __name__, url_prefix="/")


# POST:将前端的数据提交给服务器
@bp.route("LoginView", methods=["POST"])
def login_view():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    print(data)
    username = data.get('username', None)
    password = data.get('password', None)
    query = User.query.filter_by(user_name=username).first()
    print(query)
    if not query:
        message = '该用户不存在!'
        return Result.error(400,message)
    else:
        if query.password == password:
            return Result.success("登陆成功!")
        else:
            message = '密码错误,登陆失败!'
            return Result.error(400, message)


@bp.route("RegisterView", methods=["POST","GET"])
def register_view():
    data = request.get_json()
    print(data)
    if not data:
        return Result.error(400, 'post 必须是json数据')
    message = {}
    username = data.get('username', None)
    password = data.get('password', None)
    email = data.get('email', None)

    # 判断是否为空
    if 'username' not in data or not username:
        message = "请提供一个有效的用户名！"
    if 'email' not in data or not email:
        message = "请提供一个有效的邮箱地址！"
    if 'password' not in data or not password:
        message = "请提供一个有效的密码！"

    # 检查数据库中是否有该用户
    if db.session.query(User).filter(User.user_name == username).first():
        message = '用户名已存在'
    if db.session.query(User).filter(User.email == email).first():
        message = '邮箱已存在'
    if message:
        return Result.error(400, message)

    # 创建新用户
    k = 2
    user = User()
    user.from_dict(data, new_user=True, id=k)
    print(user)
    db.session.add(user)
    db.session.commit()
    k = k+1
    return Result.success("OK")
