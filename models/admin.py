from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base 
from .user import Base



class Admin(Base):
    __tablename__ = "admins"

    id = Column("id", Integer, primary_key=True)
    admin_id = Column("admin_id", Integer, nullable=False)
    admin_role = Column("admin_role", String, nullable=False)


    def __init__(self, admin_id, admin_role) -> None:
        self.admin_id = admin_id
        self.admin_role = admin_role


    def __repr__(self) -> str:
        return f"{{admin_id: {self.admin_id}, admin_role: {self.admin_role}}}"