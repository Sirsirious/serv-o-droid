from datetime import datetime

from sqlalchemy import Column, DateTime, Boolean, ForeignKey, String, Table

from app.database.database import Base, UUIDMixin
from sqlalchemy.types import Text




class ConversationMessage(UUIDMixin, Base):
    __tablename__ = 'messages'

    conversation_id = Column(String, ForeignKey('conversations.id'), index=True)
    text = Column(Text, nullable=False)
    posted_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    from_agent = Column(Boolean, nullable=False, default=False)
    intent_id = Column(String, ForeignKey('intent.id'), nullable=True)


class Conversation(UUIDMixin, Base):
    __tablename__ = 'conversations'

    started_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    is_finished = Column(Boolean, nullable=False, default=False)

