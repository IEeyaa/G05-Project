from elasticsearch import Elasticsearch

from models import Thesis

class ElasticSearch:
    def __init__(self, index_name, index_type):
        self.es = Elasticsearch("https://localhost:9200", verify_certs=False,)
        self.index_name = index_name
        self.index_type = index_type

    def search_key_thesis(self, query, count: int = 10):
        ds1 = {
            "_source": {
                "includes": ["keywords"]
            },
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["thesis_id"]
                }
            }
        }
        match_data = self.es.search(index=self.index_name, body=ds1, size=count)
        return match_data

    def search_thesis(self, query, count: int = 30):
        ds1 = {
            "_source": {
                "includes": ["thesis_id"]
            },
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["keywords"]
                }
            }
        }
        match_data = self.es.search(index=self.index_name, body=ds1, size=count)
        return match_data

    def search(self, query: str, count: int = 30):
        ds1 = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "abstract"]
                }
            }
        }
        match_data = self.es.search(index=self.index_name, body=ds1, size=count)
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
            es.index(index="ThesisInfor", body=infor)
    except Exception as e:
        print("Error:" + str(e))

