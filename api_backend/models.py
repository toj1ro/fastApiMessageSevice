import datetime
from sqlalchemy import Column, Integer, String, DateTime
from db import Base


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer)
    message_text = Column(String)
    status = Column(String, default="review")
    create_datetime = Column(DateTime, default=datetime.datetime.utcnow())
