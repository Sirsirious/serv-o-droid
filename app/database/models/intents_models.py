from datetime import datetime

from sqlalchemy import Column, DateTime, Boolean, ForeignKey, String, Table
from sqlalchemy.orm import relationship

from app.database.database import Base, UUIDMixin
from sqlalchemy.types import Text


class Intent(Base, UUIDMixin):
    __tablename__ = 'intents'
    name = Column(String(255), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class IntentSet(Base, UUIDMixin):
    __tablename__ = 'intent_set'
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class IntentMap(Base):
    __tablename__ = 'intent_map'
    intent_id = Column(String(36), ForeignKey('intents.id'),
                       nullable=False, index=True, primary_key=True)
    intent_set_id = Column(String(36), ForeignKey('intent_set.id'),
                           nullable=False, index=True, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)