from flask import Blueprint, jsonify, request
from models import Thesis, Favorites
from util import Result
from exts import db

bp = Blueprint("result", __name__, url_prefix="/")


@bp.route("InforView", methods=['POST'])
def infor_data():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    thesis_id = data.get('thesis_id', None)
    all_thesis = Thesis.query.filter_by(thesis_id=thesis_id).all()
    alldata = []
    for single_thesis in all_thesis:
        single_data = Thesis.to_dict(single_thesis)
        alldata.append(single_data)
    return Result.success(alldata)


@bp.route("CompareView", methods=['POST'])
def comp_data():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    thesis_id = data.get('thesis_id', None)
    print(thesis_id)
    all_thesis = Thesis.query.filter_by(thesis_id=thesis_id).all()
    alldata = []
    for single_thesis in all_thesis:
        single_data = Thesis.to_dict(single_thesis)
        alldata.append(single_data)
    return Result.success(alldata)


@bp.route("HomeView", methods=['GET', 'POST'])
def home_data():
    # get请求，用于初始化
    if request.method == 'GET':
        all_thesis = db.session.query(Thesis).all()
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

        thesis_id = int(data.get('thesis_id', None))
        user_id = int(data.get('user_id', None))
        if user_id == -1:
            message = "用户未登录"
            return Result.error(400, message)

        has_contain = Favorites.query.filter_by(thesis_id=thesis_id, user_id=user_id).first()

        if has_contain:
            message = "该论文已收藏"
            return Result.error(400, message)

        favor = Favorites(thesis_id=thesis_id, user_id=user_id)
        db.session.add(favor)
        db.session.commit()
        return Result.success("OK")

