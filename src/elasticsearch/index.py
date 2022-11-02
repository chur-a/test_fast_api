from elasticsearch import Elasticsearch

from src.config import config

es = Elasticsearch(config.ELASTICSEARCH_URL)

if not es.indices.exists(index='documents'):
    es.indices.create(index='documents')
