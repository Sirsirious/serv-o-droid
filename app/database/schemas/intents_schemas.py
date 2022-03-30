from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IntentBase(BaseModel):
    name: str
    description: str


class IntentCreate(IntentBase):
    pass


class IntentUpdate(IntentBase):
    pass


class Intent(IntentBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class IntentSetBase(BaseModel):
    name: str
    description: str
    active: bool


class IntentSetCreate(IntentSetBase):
    pass


class IntentSetUpdate(IntentSetBase):
    pass


class IntentSet(IntentSetBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True