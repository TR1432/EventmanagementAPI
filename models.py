from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass 

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    date = Column(Date, nullable=False )
    description = Column(String, nullable=False)