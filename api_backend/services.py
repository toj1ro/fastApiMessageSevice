from datetime import datetime, timedelta
from json import loads
from typing import Optional

from jose import jwt
from sqlalchemy.orm import Session

import models
import schemas
from kafka import KafkaConsumer, KafkaProducer


def create_message(db: Session, message: schemas.MessageSchema):
    db_message = models.Message(user_id=message.user_id, message_text=message.message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message.id


def change_status(db: Session, status: bool, message_id: int):
    choise = {True: "correct", False: "blocked"}
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    setattr(db_message, "status", choise[status])
    return db_message


def send_to_kafka(message: str, message_id: int):
    producer = KafkaProducer(bootstrap_servers='broker:9092')
    producer.send(topic='messages', key=bytes(str(message_id), encoding='utf-8'),
                  value=bytes(message, encoding='utf-8'))
