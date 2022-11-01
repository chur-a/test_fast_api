from db import Base

from sqlalchemy import Column, Integer, ARRAY, String, DateTime, func


class Documents(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    rubrics = Column(ARRAY(String))
    text = Column(String)
    created_date = Column(DateTime, server_default=func.now())
