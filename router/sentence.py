from typing import Dict, List
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.functions import mode
from db.db_connection import engine
from db.table import Sentence

router = APIRouter(prefix="/sentence")


@router.get("/query")
async def query(sentence_id: int = None, belong_document_id: int = None):
    session = sessionmaker(engine)()
    query = session.query(Sentence)
    if sentence_id is not None:
        query = query.filter(Sentence.sentence_id == sentence_id)
    if belong_document_id is not None:
        query = query.filter(Sentence.belong_document_id == belong_document_id)
    sentence = query.all()
    session.close()
    return sentence


class UpdateModel(BaseModel):
    sentence_id: int
    context: List[Dict]


@router.post("/update")
async def update(model: UpdateModel):
    session = sessionmaker(engine)()
    sentence = session.query(Sentence).filter(Sentence.sentence_id == model.sentence_id).first()
    for token in model.context:
        for token_origin in sentence.context:
            if token_origin["word_id"] == token["word_id"]:
                token_origin["word"] = token["word"]
                token_origin["label_id"] = token["label_id"]
    session.query(Sentence).filter(Sentence.sentence_id == model.sentence_id).update({"context": sentence.context})
    session.commit()
    session.close()
    return {"status": "ok"}


class AddedSentence(BaseModel):
    belong_document_id: int
    sequence: int
    context: str


@router.post("/add")
async def add(added_sentence: AddedSentence):
    context = added_sentence.context.split(" ")
    context = [{"word_id": i, "word": word, "label_id": 0} for i, word in enumerate(context)]
    sentence = Sentence(belong_document_id=added_sentence.belong_document_id, sequence=added_sentence.sequence, context=context)
    session = sessionmaker(engine)()
    session.query(Sentence).filter(Sentence.belong_document_id == added_sentence.belong_document_id, Sentence.sequence >= added_sentence.sequence).update({Sentence.sequence: Sentence.sequence + 1})
    session.add(sentence)
    session.commit()
    session.close()
    return {"status": "ok"}


class TokenModel(BaseModel):
    sentence_id: int
    word_id: int
    word: str
    label_id: int = 0


@router.post("/token/add")
async def token_add(token: TokenModel):
    session = sessionmaker(engine)()
    sentence = session.query(Sentence).filter(Sentence.sentence_id == token.sentence_id).first()
    sentence.context.insert(token.word_id, {"word_id": token.word_id, "word": token.word, "label_id": token.label_id})
    for i in range(token.word_id+1, len(sentence.context)):
        sentence.context[i]["word_id"] += 1
    session.query(Sentence).filter(Sentence.sentence_id == token.sentence_id).update({"context": sentence.context})
    session.commit()
    session.close()
    return {"status": "ok"}


@router.post("/token/delete")
async def token_delete(sentence_id: int, word_id: int):
    session = sessionmaker(engine)()
    sentence = session.query(Sentence).filter(Sentence.sentence_id == sentence_id).first()
    for token in sentence.context:
        if token["word_id"] == word_id:
            sentence.context.remove(token)
    for idx, token in enumerate(sentence.context):
        token["word_id"] = idx
    session.query(Sentence).filter(Sentence.sentence_id == sentence_id).update({"context": sentence.context})
    session.commit()
    session.close()
    return {"status": "ok"}
