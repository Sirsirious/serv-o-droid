from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Json
from app.database.models.nlu_model_registry_models import TrainingResultStatus


class NLUModelSchemaBase(BaseModel):
    name: str
    description: str


class NLUModelSchemaCreate(NLUModelSchemaBase):
    pass


class NLUModelSchemaUpdate(NLUModelSchemaBase):
    last_trained: Optional[datetime]
    filename: Optional[str]


class NLUModelSchema(NLUModelSchemaBase):
    id: str
    filename: Optional[str]
    last_trained: Optional[datetime]

    class Config:
        orm_mode = True


class NLUModelRegistryDelete(BaseModel):
    id: str


class TrainingResultSchemaBase(BaseModel):
    nlu_model_id: str


class TrainingResultSchemaCreate(TrainingResultSchemaBase):
    dataset_id: str
    parameters: Json


class TrainingResultSchemaUpdate(TrainingResultSchemaBase):
    status: TrainingResultStatus
    finished_at: Optional[datetime]
    results: Optional[Json]


class TrainingResultSchema(TrainingResultSchemaBase):
    id: str
    dataset_id: str
    status: TrainingResultStatus
    created_at: datetime
    finished_at: Optional[datetime]
    parameters: Json
    results: Optional[Json]

    class Config:
        orm_mode = True
