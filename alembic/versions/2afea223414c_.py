"""Create database

Revision ID: 2afea223414c
Revises: 
Create Date: 2022-11-14 19:59:23.198957

"""
from alembic import op
import sqlalchemy as sa

from src.elasticsearch.index import es
from src.config import config


# revision identifiers, used by Alembic.
revision = '2afea223414c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE TABLE documents ('
               'id int PRIMARY KEY,'
               'rubrics varchar,'
               'text_ varchar,'
               'created_date timestamp)')
    mapping = {
        "mappings": {
            "properties": {
                'text': {'type': 'text'}
            }
        }
    }
    if not es.indices.exists(index=config.ELASTICSEARCH_NAME_OF_INDEX):
        es.indices.create(index=config.ELASTICSEARCH_NAME_OF_INDEX, body=mapping)


def downgrade() -> None:
    op.execute('DROP TABLE IF EXISTS documents')
    es.indices.delete(index=config.ELASTICSEARCH_NAME_OF_INDEX)
