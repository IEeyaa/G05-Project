from flask import Blueprint, jsonify, request

from util import Result
from exts import db
from models import Thesis, User, Favorites

bp = Blueprint("result", __name__, url_prefix="/")


@bp.route("InforView", methods=['POST'])
def infor_data():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    thesis_id = data.get('thesis_id', None)
    thesis = Thesis.query.filter_by(thesis_id=thesis_id).first()
    return Result.success(Thesis.to_dict(thesis))


@bp.route("CompareView", methods=['POST'])
def comp_data():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    thesis_id = data.get('thesis_id', None)
    thesis = Thesis.query.filter_by(thesis_id=thesis_id).first()
    return Result.success(Thesis.to_dict(thesis))


@bp.route("HomeView", methods=['GET', 'POST'])
def home_data():
    # get请求，用于初始化
    if request.method == 'GET':
        page_id = int(request.args.get('page')) - 1
        all_thesis = Thesis.query.offset(10*page_id).limit(10).all()
        alldata = []
        for single_thesis in all_thesis:
            single_data = Thesis.to_dict(single_thesis)
            alldata.append(single_data)
        return Result.success(alldata)
    # post请求，用于处理用户收藏
    else:
        data = request.get_json()
        if not data:
            return Result.error(400, 'post 必须是json数据')

        thesis_id = data.get('thesis_id', None)
        user_name = data.get('user_name', None)
        if user_name == -1:
            message = "用户未登录"
            return Result.error(400, message)
        user_id = User.query.filter_by(user_name=user_name).first().user_id
        has_contain = Favorites.query.filter_by(thesis_id=thesis_id, user_id=user_id).first()

        if has_contain:
            message = "该论文已收藏"
            return Result.error(400, message)

        favor = Favorites(thesis_id=thesis_id, user_id=user_id)
        db.session.add(favor)
        db.session.commit()
        return Result.success("OK")


@bp.route("UserArticle", methods=['GET', 'POST'])
def user_fav_data():
    # get请求，用于初始化
    if request.method == 'GET':
        alldata = []
        user_name = request.args.get('user_name')
        if user_name == -1:
            message = "用户未登录"
            return Result.error(400, message)
        user_id = User.query.filter_by(user_name=user_name).first().user_id
        all_thesis_id = Favorites.query.filter_by(user_id=user_id).all()
        for single_thesis_id in all_thesis_id:
            single_thesis = Thesis.query.filter_by(thesis_id=single_thesis_id.thesis_id).first()
            single_data = Thesis.to_dict(single_thesis)
            alldata.append(single_data)
        return Result.success(alldata)
    else:
        data = request.get_json()
        if not data:
            return Result.error(400, 'post 必须是json数据')
        thesis_id = data.get('thesis_id', None)
        user_name = data.get('user_name', None)
        if user_name == -1:
            message = "用户未登录"
            return Result.error(400, message)
        user_id = User.query.filter_by(user_name=user_name).first().user_id
        favor = Favorites.query.filter_by(thesis_id=thesis_id, user_id=user_id).first()
        db.session.delete(favor)
        db.session.commit()
        return Result.success("OK")


@bp.route("UserView", methods=['GET', 'POST'])
def user_simple_data():
    if request.method == 'GET':
        name = request.args.get('user_name')
        user = User.query.filter_by(user_name=name).first()
        return Result.success(User.to_dict(user))
    else:
        data = request.get_json()
        if not data:
            return Result.error(400, 'post 必须是json数据')
        old_name = data.get('old_name', None)
        user_id = User.query.filter_by(user_name=old_name).first().user_id
        if not user_id:
            message = "用户不存在"
            return Result.error(400, message)
        new_name = data.get('new_name', None)
        city = data.get('city', None)
        motto = data.get('motto', None)
        email = data.get('email', None)
        user = User.query.filter_by(user_id=user_id).first()
        user.user_name = new_name
        user.city = city
        user.motto = motto
        user.email = email
        db.session.commit()
        return Result.success("OK")

