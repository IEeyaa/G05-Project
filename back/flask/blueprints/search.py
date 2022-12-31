from flask import Blueprint, request

from flask_file.es import ElasticSearch
from flask_file.models import Thesis
from flask_file.util import Result


bp = Blueprint("search", __name__, url_prefix="/")


# @bp.route("SearchView", methods=["POST"])
# def get_es():
#     key_word = request.get_json()
#     print(key_word)
#     keyword = str(key_word)
#     es = ElasticSearch(index_name="thesisinfo", index_type="test-type")
#     data = es.search(keyword)
#     print(data)
#     address_data = data["hits"]["hits"]
#     address_list = []
#     for item in address_data:
#         address_list.append(item["_source"])
#     return Result.success(address_list)


@bp.route("SearchView", methods=["POST"])
def get_es():
    data = request.get_json()
    key_word = data.get('word', None)
    answers1 = Thesis.query.filter(Thesis.title.like("%" + key_word + "%")
                                  if key_word is not None else "").all()
    answers2 = Thesis.query.filter(Thesis.abstract.like("%" + key_word + "%")
                                  if key_word is not None else "").all()
    alldata = []
    count = 0
    for single_thesis in answers1:
        single_data = Thesis.to_dict(single_thesis)
        alldata.append(single_data)
        count = count + 1
        if count > 100:
            break
    for single_thesis in answers2:
        single_data = Thesis.to_dict(single_thesis)
        alldata.append(single_data)
        count = count + 1
        if count > 100:
            break
    return Result.success(alldata)

