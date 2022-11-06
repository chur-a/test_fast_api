import csv
import os.path

from sqlalchemy import text

from src.db.db import engine
from src.elasticsearch.index import es
from src.config import config


def database_creation():
    with engine.connect() as conn:
        stmt = text('DROP TABLE IF EXISTS documents')
        conn.execute(stmt)
        stmt = text('CREATE TABLE documents ('
                    'id int PRIMARY KEY,'
                    'rubrics varchar,'
                    'text_ varchar,'
                    'created_date timestamp)')
        conn.execute(stmt)
    mapping = {
        "mappings": {
            "properties": {
                'text': {'type': 'text'}
            }
        }
    }
    es.indices.delete(index=config.ELASTICSEARCH_NAME_OF_INDEX)
    es.indices.create(index=config.ELASTICSEARCH_NAME_OF_INDEX, body=mapping)


def download_dataset():
    with open('././dataset.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        i = 0
        with engine.connect() as conn:
            for line in reader:
                stmt = text("INSERT INTO documents VALUES "
                            "(:x, :y, :z, :t)")
                conn.execute(stmt, {'x': i, 'y': line[2], 'z': line[0], 't': line[1]})
                doc = {'text': line[0]}
                es.index(index=config.ELASTICSEARCH_NAME_OF_INDEX, body=doc, id=i)
                i += 1


if __name__ == '__main__':
    database_creation()
    if os.path.exists('dataset.csv'):
        download_dataset()
