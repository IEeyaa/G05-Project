# 和搜索有关的蓝图页
from flask import Blueprint

bp = Blueprint("search", __name__, url_prefix="/")


@bp.route("/")
def index():
    pass
