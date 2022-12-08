from flask import Blueprint, jsonify, request
from models import Thesis
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
    # post请求，用于排序后展示
    else:
        data = request.get_json()
        if not data:
            return Result.error(400, 'post 必须是json数据')
        rule = int(data.get('rule', None))
        # 排序方式
        if rule == 1:
            all_thesis = db.session.query(Thesis).order_by(Thesis.thesis_id).all()
        elif rule == 2:
            all_thesis = db.session.query(Thesis).order_by(Thesis.title).all()
        elif rule == 3:
            all_thesis = db.session.query(Thesis).order_by(Thesis.publication_date.desc()).all()
        else:
            all_thesis = db.session.query(Thesis).order_by(Thesis.citation_num).all()

        alldata = []
        for single_thesis in all_thesis:
            single_data = Thesis.to_dict(single_thesis)
            alldata.append(single_data)
        return Result.success(alldata)

