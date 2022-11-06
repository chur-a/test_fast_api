from datetime import datetime

from pydantic import BaseModel


class DocumentBase(BaseModel):
    rubrics: str
    text: str


class DocumentModel(DocumentBase):
    id: int
    created_date: datetime
