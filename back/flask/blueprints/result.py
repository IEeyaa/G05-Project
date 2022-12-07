# 和结果展示与分析有关的蓝图页
# About InforView.vue and HomeView.vue
from flask import Blueprint, jsonify, request
from models import Thesis
from util import Result
from exts import db

bp = Blueprint("result", __name__, url_prefix="/")


@bp.route("InforView", methods=['GET', 'POST'])
def return_data():
    # get请求，用于Home
    if request.method == 'GET':
        all_thesis = db.session.query(Thesis).all()
        alldata = []
        for single_thesis in all_thesis:
            single_data = Thesis.to_dict(single_thesis)
            alldata.append(single_data)
        return Result.success(alldata)
    # post请求，用于Infor
    else:
        data = request.get_json()
        if not data:
            return Result.error(400, 'POST 必须是json数据')
        thesis_id = data.get('thesis_id', None)
        all_thesis = Thesis.query.filter_by(thesis_id=thesis_id).all()
        alldata = []
        for single_thesis in all_thesis:
            single_data = Thesis.to_dict(single_thesis)
            alldata.append(single_data)
        return Result.success(alldata)
