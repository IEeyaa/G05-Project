# 和结果展示与分析有关的蓝图页
# About InforView.vue and HomeView.vue
from flask import Blueprint
from models import Thesis
from util import Result
from exts import db

bp = Blueprint("result", __name__, url_prefix="/result")


@bp.route("single")
def single():
    query = {}
    query = db.session.query(Thesis.thesis_id, Thesis.title, Thesis.author, Thesis.publication_date, Thesis.journal, Thesis.abstract, Thesis.link, Thesis.citation_num, Thesis. rating).order_by(Thesis.thesis_id.asc()).all()
    res = []
    content = {}
    for i in query:
        content = {'thesis_id': i[0], 'title': i[1], 'author': i[2], 'publication_date': i[3], 'journal': i[4], 'abstract': i[5], 'link': i[6], 'citation_num': i[7], 'rating': i[8]}
        res.append(content)
        content = {}
    print (res)
    return Result.success(res)