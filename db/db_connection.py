from sqlalchemy import create_engine
from db.table import Base

engine = create_engine("mysql+pymysql://root:02080328@localhost:3306/annotator")

Base.metadata.create_all(engine)