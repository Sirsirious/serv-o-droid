from datetime import datetime

from sqlalchemy import Column, DateTime, Boolean, ForeignKey, String, Table
from sqlalchemy.orm import relationship

from app.database.database import Base, UUIDMixin
from sqlalchemy.types import Text


class Dataset(Base, UUIDMixin):
    __tablename__ = 'datasets'
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    language = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class DatasetEntry(Base):
    __tablename__ = 'dataset_entries'
    dataset_id = Column(String(36), ForeignKey('datasets.id'),
                        nullable=False, index=True, primary_key=True)
    message_id = Column(String(36), ForeignKey('messages.id'),
                        nullable=False, index=True, primary_key=True)
    intent_id = Column(String(36), ForeignKey('intents.id'), nullable=True)
    dataset = relationship('datasets', backref='dataset_entries')
    messages = relationship('messages', backref='dataset_entries')
    intents = relationship('intents', backref='dataset_entries')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

