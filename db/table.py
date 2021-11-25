from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, JSON, BigInteger, TIMESTAMP

Base = declarative_base()


class Label(Base):
    __tablename__ = "label"
    label_id = Column(BigInteger, primary_key=True)
    name = Column(String(64))
    description = Column(String(255))


class Sentence(Base):
    __tablename__ = "sentence"
    sentence_id = Column(BigInteger, primary_key=True)
    belong_document_id = Column(BigInteger)
    sequence = Column(BigInteger)
    context = Column(JSON)


class Document(Base):
    __tablename__ = "document"
    document_id = Column(BigInteger, primary_key=True)
    uuid = Column(String(64))
    event_name = Column(String(255))
    status = Column(String(64))
    create_time = Column(TIMESTAMP)
