from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from db.db_connection import engine
from db.table import Label

router = APIRouter(prefix="/label")


@router.get("/all")
async def all():
    session = sessionmaker(engine)()
    labels = session.query(Label).all()
    session.close()
    return labels


@router.get("/{label_id}")
async def id_get(label_id: int):
    session = sessionmaker(engine)()
    label = session.query(Label).filter(Label.label_id==label_id).first()
    session.close()
    return label
