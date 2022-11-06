from elasticsearch import Elasticsearch

from src.config import config


es = Elasticsearch(config.ELASTICSEARCH_URL, ca_certs=config.ELASTICSEARCH_PATH_TO_CERTIFICATE, request_timeout=40)
