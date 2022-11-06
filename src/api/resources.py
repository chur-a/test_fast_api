from fastapi import APIRouter, status, Query, HTTPException
from sqlalchemy import text

from .schemas import DocumentModel
from src.db.db import engine
from src.elasticsearch.index import es
from src.config import config


router = APIRouter()


@router.get('/get_docs', response_model=list[DocumentModel], summary='Список первых 20 документов по дате создания')
def get(query_text: str = Query(title='Текстовый запрос')):
    query_body = {'query':
                  {'match':
                   {'text': query_text}
                   }
                  }
    res = es.search(index=config.ELASTICSEARCH_NAME_OF_INDEX, body=query_body)
    list_of_ids = []
    for doc in res['hits']['hits']:
        list_of_ids.append(int(doc['_id']))
    stmt = text('SELECT * '
                'FROM documents '
                'WHERE id = ANY(:x) '
                'ORDER BY created_date DESC '
                'LIMIT 20 ')
    with engine.connect() as conn:
        result = conn.execute(stmt, {'x': list_of_ids})
    return [DocumentModel(id=r[0], rubrics=r[1], text=r[2], created_date=r[3]) for r in result.fetchall()]


@router.delete('/delete_doc', summary='Удалить документ')
def delete(document_id: int = Query(title='Id удаляемого документа', ge=0)):
    stmt = text('DELETE FROM documents '
                'WHERE id = :x')
    with engine.connect() as conn:
        result = conn.execute(stmt, {'x': document_id})
    if not result.rowcount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Документа с данным id не существует.')
    es.delete(index=config.ELASTICSEARCH_NAME_OF_INDEX, id=document_id)
    return {'Successful operation': True}
