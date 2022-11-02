from fastapi import APIRouter, status, Query, HTTPException
from sqlalchemy import text

from .schemas import DocumentsResponse
from src.db.db import engine
from src.elasticsearch.index import es


router = APIRouter()


@router.get('/get_docs', response_model=DocumentsResponse, summary='Список первых 20 документов по дате создания')
def get(query_text: str = Query(title='Текстовый запрос')):
    query_body = {'query':
                  {'match':
                   {'message': query_text}
                   }
                  }
    res = es.search(index='index', body=query_body)
    list_of_ids = []
    for doc in res['hits']['hits']:
        list_of_ids.append(int(doc['_id']))
    stmt = text('SELECT *'
                'FROM documents'
                'WHERE id IN :x'
                'ORDER BY created_date'
                'LIMIT 20')
    with engine.connec() as conn:
        result = conn.execute(stmt, {'x': list_of_ids})
    return result.fetchall() #FIXME


@router.delete('/delete_doc', summary='Удалить документ')
def delete(document_id: int = Query(title='Id удаляемого документа', ge=0)):
    stmt = text('DELETE FROM documents'
                'WHERE id = :x')
    with engine.connect() as conn:
        result = conn.execute(stmt, {'x': document_id})
    if not result.rowcount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Документа с данным id не существует.')
    es.delete(index='index', id=document_id)
    return {'Successful operation': True}
