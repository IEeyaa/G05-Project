from flask import Blueprint, jsonify, request

from util import Result
from exts import db
from models import Thesis, User, Favorites
import pandas as pd
import config
from sqlalchemy import create_engine

bp = Blueprint("result", __name__, url_prefix="/")

def get_rating(citation_rank:int, date_rank:int, total:int, rank_thre:int):
    citation_rating = date_rating = 0
    if citation_rank > rank_thre:         #citation_num<18
        citation_rating = ((total-citation_rank)/(total-rank_thre))*0.4+0.2
    else:
        citation_rating = ((rank_thre-citation_rank)/(rank_thre-1))*0.4+0.6
    if date_rank > 3500:
        date_rating = ((total-date_rank)/(total-3500))*0.4+0.2
    else:
        date_rating = ((3500-date_rank)/(3500-1))*0.4+0.6
    return citation_rating, date_rating

@bp.route("CompareThesis", methods=['POST'])
def comp_thesis():
    data = request.get_json()
    if not data:
        return Result.error(400, 'post 必须是json数据')
    thesis_id1 = int(data['thesis_id1'])
    thesis_id2 = int(data['thesis_id2'])
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(config.USERNAME, config.PASSWORD, config.HOSTNAME, config.PORT, config.DATABASE))
    sql = '''
          select thesis_id, publication_date, citation_num from thesis;
          '''
    df = pd.read_sql_query(sql, engine)
    df['publication_date'] = df['publication_date'].astype('datetime64[ns]')
    df['citation_rank'] = df.citation_num.rank(method='max', ascending=False)
    df['date_rank'] = df.publication_date.rank(method='max', ascending=False)
    print(df)
    print(df.describe())
    citation_rank1 = date_rank1 = -1
    citation_rank2 = date_rank2 = -1
    citation_thre = 18
    rank_thre = 675
    for row in df.itertuples():
        if row[3] == citation_thre:
            rank_thre = row[4]
        if int(row[1]) == thesis_id1:
            print(row)
            citation_rank1 = row[4]
            date_rank1 = row[5]
        if int(row[1]) == thesis_id2:
            print(row)
            citation_rank2 = row[4]
            date_rank2 = row[5]
    if date_rank1 == -1 or date_rank2 == -1:
        return Result.error("403", "无效论文编号")
    total = len(df)
    print(citation_rank1, date_rank1, citation_rank2, date_rank2)
    citation_rating1, date_rating1 = get_rating(citation_rank1, date_rank1, total, rank_thre)
    citation_rating2, date_rating2 = get_rating(citation_rank2, date_rank2, total, rank_thre)
    ret = [{'citation_rating1': citation_rating1, 'citation_rating2': citation_rating2, 
            'date_rating1': date_rating1, 'date_rating2': date_rating2}]
    return Result.success(ret)



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

