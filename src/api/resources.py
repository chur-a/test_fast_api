from fastapi import APIRouter, status, Query, HTTPException
from sqlalchemy import text

from .schemas import DocumentsResponse
from src.db.db import engine


router = APIRouter()


@router.get('/get_docs', response_model=DocumentsResponse, summary='Список первых 20 документов по дате создания')
def get(text: str = Query(title='Текстовый запрос')):
    #Запрос в индекс
    pass


@router.delete('/delete_doc', summary='Удалить документ')
def delete(document_id: int = Query(title='Id удаляемого документа', ge=0)):
    stmt = text('DELETE FROM documents'
                'WHERE id = :x')
    with engine.connect() as conn:
        result = conn.execute(stmt, {'x': document_id})
    if not result.rowcount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Документа с данным id не существует.')
    return {'Successful operation': True}
