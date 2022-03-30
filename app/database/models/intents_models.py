from datetime import datetime

from sqlalchemy import Column, DateTime, Boolean, ForeignKey, String, Table

from app.database.database import Base, UUIDMixin
from sqlalchemy.types import Text


class Intent(Base, UUIDMixin):
    __tablename__ = 'intent'
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