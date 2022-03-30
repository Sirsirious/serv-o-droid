from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal, get_db
from app.database.schemas import intents_schemas
from app.services import intents_crud

router = APIRouter(prefix='/intents')


@router.get('/', tags=['intents'], response_model=List[intents_schemas.Intent])
async def get_all_intents(db: Session = Depends(get_db)):
    return intents_crud.get_intents(db)


@router.get('/{intent_id}', tags=['intents'], response_model=intents_schemas.Intent)
async def get_intent_by_id(intent_id: str, db: Session = Depends(get_db)):
    return intents_crud.get_intent(db, intent_id)


@router.post('/', tags=['intents'], response_model=intents_schemas.Intent)
async def create_intent(intent: intents_schemas.IntentCreate, db: Session = Depends(get_db)):
    existing_intent = intents_crud.get_intent_by_name(db=db, name=intent.name)
    if existing_intent:
        raise HTTPException(status_code=400, detail="Intent with this name already exists")
    return intents_crud.create_intent(db, intent)


@router.put('/{intent_id}', tags=['intents'], response_model=intents_schemas.Intent)
async def update_intent(intent_id: str, intent: intents_schemas.IntentUpdate, db: Session = Depends(get_db)):
    return intents_crud.update_intent(db=db, intent_id=intent_id, intent=intent)


@router.put('/sets/{intent_set_id}/add_intent', tags=['intents'], response_model=intents_schemas.Intent)
async def add_intent_to_intent_set(intent_set_id: str, intent_id: str, db: Session = Depends(get_db)):
    updated_intent = intents_crud.add_intent_to_intent_set(db=db, intent_set_id=intent_set_id, intent_id=intent_id)
    if updated_intent is None:
        raise HTTPException(status_code=404, detail="Intent or intent set not found")
    return updated_intent


# IntentSets

@router.get('/sets/', tags=['intents'], response_model=List[intents_schemas.IntentSet])
async def get_all_intent_sets(db: Session = Depends(get_db)):
    return intents_crud.get_intent_sets(db)


@router.get('/sets/{intent_set_id}', tags=['intents'], response_model=intents_schemas.IntentSet)
async def get_intent_set_by_id(intent_set_id: str, db: Session = Depends(get_db)):
    return intents_crud.get_intent_set(db, intent_set_id)


@router.post('/sets/', tags=['intents'], response_model=intents_schemas.IntentSet)
async def create_intent_set(intent_set: intents_schemas.IntentSetCreate, db: Session = Depends(get_db)):
    return intents_crud.create_intent_set(db, intent_set)


@router.put('/sets/{intent_set_id}', tags=['intents'], response_model=intents_schemas.IntentSet)
async def update_intent_set(intent_set_id: str, intent_set: intents_schemas.IntentSetUpdate,
                            db: Session = Depends(get_db)):
    return intents_crud.update_intent_set(db=db, intent_set_id=intent_set_id, intent_set=intent_set)
