from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class DatasetBase(BaseModel):
    name: str
    description: Optional[str] = None
    language: Optional[str] = 'English'


class DatasetCreate(DatasetBase):
    pass


class DatasetUpdate(DatasetBase):
    pass


class DatasetDelete(BaseModel):
    id: str


class Dataset(DatasetBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DatasetEntryBase(BaseModel):
    pass


class DatasetEntryCreate(DatasetEntryBase):
    dataset_id: str
    message_id: str
    intent_id: str


class DatasetEntryUpdate(DatasetEntryBase):
    intent_id: str


class DataSetEntryDelete(BaseModel):
    dataset_id: str
    message_id: str


class DatasetEntry(DatasetEntryBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

