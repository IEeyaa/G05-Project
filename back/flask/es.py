from elasticsearch import Elasticsearch

from models import Thesis


class ElasticSearch():
    def __init__(self, index_name, index_type):
        self.es = Elasticsearch()
        self.index_name = index_name
        self.index_type = index_type

    def search(self, query, count: int = 30):
        ds1 = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "abstract"]
                }
            }
        }
        match_data = self.es.search(index=self.index_name, doc_type=self.index_type, body=ds1, size=count)
        return match_data

def get_data():
    query = Thesis.query.filter_by(Thesis.thesis_id, Thesis.title, Thesis.abstract).all()
    return query


def create_es_data():
    es = Elasticsearch()
    try:
        results = get_data()
        for row in results:
            infor = {
                "thesis_id": row[0],
                "title": row[1],
                "abstract": row[2]
            }
            es.index(index="ThesisInfor", doc_type="test-type", body=infor)
    except Exception as e:
        print("Error:" + str(e))

