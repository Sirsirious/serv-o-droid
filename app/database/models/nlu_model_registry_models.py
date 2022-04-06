from datetime import datetime
import enum

from sqlalchemy import Column, DateTime, Boolean, ForeignKey, String, Table, JSON, Enum
from sqlalchemy.orm import relationship

from app.database.database import Base, UUIDMixin
from sqlalchemy.types import Text


class NLUModel(Base, UUIDMixin):
    __tablename__ = 'nlu_models'

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    filename = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    last_trained_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return '<NLUModel %r>' % self.name


class TrainingResultStatus(enum.Enum):
    finished = 'finished'
    failed = 'failed'
    pending = 'pending'


class TrainingResult(Base, UUIDMixin):
    __tablename__ = 'training_results'

    nlu_model_id = Column(String(36), ForeignKey('nlu_models.id'), nullable=False)
    dataset_id = Column(String(36), ForeignKey('datasets.id'), nullable=False)
    status = Column(Enum(TrainingResultStatus), nullable=False, default=TrainingResultStatus.pending)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True, default=datetime.utcnow)
    parameters = Column(JSON, nullable=False)
    results = Column(JSON, nullable=True)
    dataset = relationship('datasets', backref='dataset_entries')

    def __repr__(self):
        return '<TrainingResults %r>' % self.id