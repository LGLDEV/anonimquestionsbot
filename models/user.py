from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base 


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, nullable=False)


    def __init__(self, user_id, lang) -> None:
        self.user_id = user_id


    def __repr__(self) -> str:
        return f"{{user_id: {self.user_id}}}"