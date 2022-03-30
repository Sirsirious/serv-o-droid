from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class ConversationMessageBase(BaseModel):
    text: str
    from_agent: Optional[bool] = False


class ConversationMessageCreate(ConversationMessageBase):
    pass


class ConversationMessageUpdate(ConversationMessageBase):
    intent_id: str


class ConversationMessage(ConversationMessageBase):
    id: str
    conversation_id: str
    posted_at: Optional[datetime]
    intent_id: Optional[str]

    class Config:
        orm_mode = True


class ConversationBase(BaseModel):
    pass


class ConversationCreate(ConversationBase):
    pass


class Conversation(ConversationBase):
    id: str
    started_at: datetime
    finished_at: Optional[datetime] = None
    is_finished: bool
    messages: List[ConversationMessage] = []

    class Config:
        orm_mode = True

