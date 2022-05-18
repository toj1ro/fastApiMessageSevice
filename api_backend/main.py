from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import models
import schemas
import services
from db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/message")
async def message(message: schemas.MessageSchema, db: Session = Depends(get_db)):
    message_id = services.create_message(db, message)
    services.send_to_kafka(message.message, message_id)
    return {"message": "OK"}


@app.post("/api/v1/message_confirmation")
async def message_confirmation(status: schemas.StatusSchema, db: Session = Depends(get_db)):
    return services.change_status(db, status.success, status.message_id)
