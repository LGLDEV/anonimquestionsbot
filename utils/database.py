from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

from models import Base

engine = create_engine('sqlite:///mydb.db')

Session = sessionmaker(bind=engine)
session = Session()

def create_db():
    Base.metadata.create_all(bind=engine)


