from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from db.db_connection import engine
from db.table import Document, Sentence
from pydantic import BaseModel
from snowflake import IdWorker

router = APIRouter(prefix="/document")
document_id_worker = IdWorker(0, 0, 0)
sentence_id_worker = IdWorker(0, 1, 0)


@router.get("/query")
async def query(document_id: str = None, page: int = -1, size: int = -1):
    session = sessionmaker(engine)()
    query = session.query(Document)
    if document_id is not None:
        query = query.filter(Document.document_id == document_id)
    if page >= 0 and size >= 0:
        query = query.limit(size).offset(page * size)
    documents = query.all()
    session.close()
    return documents


class DocumentModel(BaseModel):
    document_id: str = None
    uuid: str
    name: str
    status: str
    context: str = None


@router.post("/update")
async def update(model: DocumentModel):
    print(model.document_id)
    session = sessionmaker(engine)()
    session.query(Document).filter(Document.document_id == model.document_id).update({
        Document.uuid: model.uuid,
        Document.name: model.name,
        Document.status: model.status
    })
    session.commit()
    session.close()
    return {"status": "ok"}


@router.post("/add")
async def add(model: DocumentModel):
    raw_sentences = model.context.split("\n")
    document = Document(document_id=document_id_worker.get_id(), uuid=model.uuid, name=model.name)
    session = sessionmaker(engine)()
    sentences = []
    for seq, raw_sentence in enumerate(raw_sentences):
        tokens = raw_sentence.split(" ")
        tokens = [{"word_id": i, "word": word, "label_id": 0} for i, word in enumerate(tokens)]
        sentence = Sentence(sentence_id=sentence_id_worker.get_id(),
                            belong_document_id=document.document_id,
                            sequence=seq,
                            context=tokens)
        sentences.append(sentence)
    session.add_all(sentences)
    session.add(document)
    session.commit()
    session.close()
    return {"status": "ok"}