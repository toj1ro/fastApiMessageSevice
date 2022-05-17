from pydantic import BaseModel


class MessageSchema(BaseModel):
    user_id: int
    message: str


class StatusSchema(BaseModel):
    message_id: int
    success: bool
