# 和搜索有关的蓝图页
# About MainView.vue
from flask import Blueprint, request
from util import Result
from es import ElasticSearch

bp = Blueprint("search", __name__, url_prefix="/")


@bp.route("SearchView", methods=["POST"])
def get_es():
    key_word = request.get_json()
    print(key_word)
    keyword = str(key_word)
    es = ElasticSearch(index_name="thesisinfo", index_type="test-type")
    data = es.search(keyword)
    print(data)
    address_data = data["hits"]["hits"]
    address_list = []
    for item in address_data:
        address_list.append(item["_source"])
    return Result.success(address_list)
