from datetime import date
from typing import List

from pydantic import BaseModel


class DocumentBase(BaseModel):
    rubrics: List[str]
    text: str


class DocumentModel(DocumentBase):
    id: int
    created_date: date


class DocumentsResponse(DocumentModel):
    documents: List[DocumentModel] = []

