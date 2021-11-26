from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, JSON, Integer, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp

Base = declarative_base()


class Label(Base):
    __tablename__ = "label"
    label_id = Column(Integer, primary_key=True)
    name = Column(String(64))
    description = Column(String(255))


class Sentence(Base):
    __tablename__ = "sentence"
    sentence_id = Column(String(64), primary_key=True)
    belong_document_id = Column(String(64))
    sequence = Column(Integer)
    context = Column(JSON)


class Document(Base):
    __tablename__ = "document"
    document_id = Column(String(64), primary_key=True)
    uuid = Column(String(64))
    name = Column(String(255))
    status = Column(String(64), default="uncompleted")
    create_time = Column(TIMESTAMP, default=current_timestamp())
