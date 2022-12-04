# 和搜索有关的蓝图页
# About MainView.vue
from flask import Blueprint

bp = Blueprint("search", __name__, url_prefix="/")


@bp.route("Search")
def Search():
    pass