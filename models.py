from sqlalchemy import Column, Integer, String
from database import Base

class CapyInDB(Base):
    __tablename__ = 'capys'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String,index=True)
    description = Column(String, index=True)
    photo = Column(String,index=True)
