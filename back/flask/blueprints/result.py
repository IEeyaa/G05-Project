from flask import Blueprint, request
from sqlalchemy import create_engine, func
from simhash import Simhash
import sys

from flask_file.util import Result
from flask_file.models import *
from flask_file import config
import pandas as pd

sys.path.append("..")

bp = Blueprint("result", __name__, url_prefix="/")


@bp.route("GetInfor", methods=['POST'])
def get_infor_data():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    thesis_id = data.get('thesis_id', None)
    thesis = Thesis.query.filter_by(thesis_id=thesis_id).first()
    return Result.success(Thesis.to_dict(thesis))


@bp.route("InforView", methods=['GET'])
def infor_data():
    thesis_id = int(request.args.get('thesis_id'))
    thesis = Thesis.query.filter_by(thesis_id=thesis_id).first()
    # 关键词
    all_keys = []
    all_keys_string = ""
    keywords = Keyword.query.all()
    for item in keywords:
        if item.data in thesis.title or item.data in thesis.abstract:
            all_keys.append(item.data)
            all_keys_string = all_keys_string + str(item.data)
    # 相关论文
    all_thesis = Thesis.query.offset(200).limit(400).all()
    min_score = 0.7
    count = 0
    max_count = 20
    related = []
    for single in all_thesis:
        temp_score = simhash_similarity(single.title, all_keys_string) * 0.7 + \
                     simhash_similarity(single.abstract, all_keys_string) * 0.3
        if temp_score > min_score:
            count = count + 1
            related.append(Thesis.to_dict(single))
        if count > max_count:
            break
    alldata = [Thesis.to_dict(thesis), all_keys]
    return Result.success_similar(alldata, related)


def simhash_similarity(text1, text2):
    """
    :param tex1: 文本1
    :param text2: 文本2
    :return: 返回两篇文章的相似度
    """
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)
    max_hashbit = max(len(bin(aa_simhash.value)), (len(bin(bb_simhash.value))))
    # 汉明距离
    distince = aa_simhash.distance(bb_simhash)
    similar = 1 - distince / max_hashbit
    return similar


def get_rating(citation_rank: int, date_rank: int, total: int, rank_thre: int):
    if citation_rank > rank_thre:
        citation_rating = ((total - citation_rank) / (total - rank_thre)) * 0.4 + 0.2
    else:
        citation_rating = ((rank_thre - citation_rank) / (rank_thre - 1)) * 0.4 + 0.6
    if date_rank > 3500:
        date_rating = ((total - date_rank) / (total - 3500)) * 0.4 + 0.2
    else:
        date_rating = ((3500 - date_rank) / (3500 - 1)) * 0.4 + 0.6
    citation_rating = round(citation_rating * 5, 2)
    date_rating = round(date_rating * 5, 2)
    return citation_rating, date_rating


@bp.route("CompareThesis", methods=['POST'])
def comp_thesis():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    thesis_id1 = int(data['thesis_id1'])
    thesis_id2 = int(data['thesis_id2'])
    keyword = str(data['key_word'])
    engine = create_engine(
        'mysql+pymysql://{}:{}@{}:{}/{}'.format(config.USERNAME, config.PASSWORD, config.HOSTNAME, config.PORT,
                                                config.DATABASE))
    sql = '''
          select thesis_id, publication_date, citation_num from thesis;
          '''
    df = pd.read_sql_query(sql, engine)
    df['publication_date'] = df['publication_date'].astype('datetime64[ns]')
    df['citation_rank'] = df.citation_num.rank(method='max', ascending=False)
    df['date_rank'] = df.publication_date.rank(method='max', ascending=False)
    citation_rank1 = date_rank1 = -1
    citation_rank2 = date_rank2 = -1
    citation_thre = 18
    rank_thre = 675
    for row in df.itertuples():
        if row[3] == citation_thre:
            rank_thre = row[4]
        if int(row[1]) == thesis_id1:
            citation_rank1 = row[4]
            date_rank1 = row[5]
        if int(row[1]) == thesis_id2:
            citation_rank2 = row[4]
            date_rank2 = row[5]
    if date_rank1 == -1 or date_rank2 == -1:
        return Result.error("403", "无效论文编号")
    total = len(df)
    Thesis1 = Thesis.query.filter_by(thesis_id=thesis_id1).first()
    Thesis2 = Thesis.query.filter_by(thesis_id=thesis_id2).first()
    key_rating1 = simhash_similarity(Thesis1.title, keyword) * 0.7 + simhash_similarity(Thesis1.abstract, keyword) * 0.3
    key_rating2 = simhash_similarity(Thesis2.title, keyword) * 0.7 + simhash_similarity(Thesis2.abstract, keyword) * 0.3
    key_rating1 = round(key_rating1 * 5, 2)
    key_rating2 = round(key_rating2 * 5, 2)
    similarity = simhash_similarity(Thesis1.title, Thesis2.title) * 0.7 + simhash_similarity(Thesis1.abstract,
                                                                                             Thesis2.abstract) * 0.3
    citation_rating1, date_rating1 = get_rating(citation_rank1, date_rank1, total, rank_thre)
    citation_rating2, date_rating2 = get_rating(citation_rank2, date_rank2, total, rank_thre)
    ret = {
        'citation_rating1': citation_rating1, 'citation_rating2': citation_rating2,
        'key_rating1': key_rating1, 'key_rating2': key_rating2,
        'date_rating1': date_rating1, 'date_rating2': date_rating2,
        'similarity': similarity,
    }
    return Result.success(ret)


@bp.route("HomeView", methods=['GET', 'POST'])
def home_data():
    # get请求，用于初始化
    if request.method == 'GET':
        page_id = int(request.args.get('page')) - 1
        all_thesis = Thesis.query.offset(10 * page_id).limit(10).all()
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


@bp.route("/StatisticsKeyView", methods=['GET'])
def graph_key_data():
    # get请求，用于初始化
    page_id = int(request.args.get('page')) - 1
    all_keys = Keyword.query.order_by(Keyword.value.desc()).offset(20 * page_id).limit(20).all()
    alldata = []
    for single in all_keys:
        alldata.append([single.data, single.value])
    return Result.success(alldata)


@bp.route("/StatisticsDateView", methods=['GET'])
def graph_date_data():
    # get请求，用于初始化
    if request.method == 'GET':
        start_day = request.args.get('start_month') + "-01"
        end_day = request.args.get('end_month') + "-01"
        all_Numbers = db.session.query(func.date_format(Thesis.publication_date, "%Y-%m"),
                                       func.count(Thesis.publication_date))\
            .filter(Thesis.publication_date.between(start_day, end_day))\
            .group_by(func.month(Thesis.publication_date)).order_by(Thesis.publication_date).all()
        alldata = []
        for item in all_Numbers:
            alldata.append([item[0], item[1]])
        return Result.success(alldata)
