from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from sqlalchemy.orm import Session

import models
import schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"


def create_message(db: Session, message: schemas.MessageSchema):
    db_message = models.Message(user_id=message.user_id, message_text=message.message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def change_status(db: Session, status: bool, message_id: int):
    choise = {True: "correct", False: "blocked"}
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    setattr(db_message, "status", choise[status])
    return db_message


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60 * 60 * 60 * 60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)
    return encoded_jwt



def get_token_by_listener():
    return create_access_token({"role": "post_message_confirm"})


print(get_token_by_listener())
