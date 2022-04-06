from typing import List

from fastapi import APIRouter, Depends
from requests import Session

from app.database.database import get_db
from app.database.schemas import dataset_schema
from app.services import datasets_crud

router = APIRouter(prefix='/datasets')


@router.get('/', tags=['datasets'], response_model=List[dataset_schema.Dataset])
def list_datasets(db: Session = Depends(get_db)):
    return datasets_crud.get_datasets(db=db)


@router.get('/{dataset_id}', tags=['datasets'], response_model=dataset_schema.Dataset)
def get_dataset(dataset_id: str, db: Session = Depends(get_db)):
    return datasets_crud.get_dataset(db=db, dataset_id=dataset_id)


@router.post('/', tags=['datasets'], response_model=dataset_schema.Dataset)
def create_dataset(dataset_data: dataset_schema.DatasetCreate, db: Session = Depends(get_db)):
    return datasets_crud.create_dataset(db=db, dataset_in=dataset_data)


@router.delete('/{dataset_id}', tags=['datasets'], response_model=dataset_schema.Dataset)
def delete_dataset(dataset_id: str, db: Session = Depends(get_db)):
    return datasets_crud.delete_dataset(db=db, dataset_id=dataset_id)


@router.patch('/{dataset_id}', tags=['datasets'], response_model=dataset_schema.Dataset)
def update_dataset(dataset_id: str, dataset_data: dataset_schema.DatasetUpdate, db: Session = Depends(get_db)):
    return datasets_crud.update_dataset(db=db, dataset_id=dataset_id, dataset_in=dataset_data)


# Dataset Entries #
@router.patch('/{dataset_id}/entries', tags=['datasets'], response_model=List[dataset_schema.DatasetEntry])
def get_dataset_entries(dataset_id: str, db: Session = Depends(get_db)):
    return datasets_crud.get_dataset_entries(db=db, dataset_id=dataset_id)


@router.post('/{dataset_id}/entries', tags=['datasets'], response_model=dataset_schema.DatasetEntry)
def add_datset_entry(dataset_id, dataset_entry_data: dataset_schema.DatasetEntryCreate, db: Session = Depends(get_db)):
    return datasets_crud.add_dataset_entry(db=db, dataset_id=dataset_id, dataset_entry_in=dataset_entry_data)


@router.get('/entries/{dataset_entry_id}', tags=['datasets'], response_model=dataset_schema.DatasetEntry)
def get_dataset_entry_by_id(dataset_entry_id: str, db: Session = Depends(get_db)):
    return datasets_crud.get_dataset_entry_by_id(db=db, dataset_entry_id=dataset_entry_id)


@router.patch('/entries/{dataset_entry_id}', tags=['datasets'], response_model=dataset_schema.DatasetEntry)
def update_dataset_entry(dataset_entry_id: str,
                         dataset_entry_data: dataset_schema.DatasetEntryUpdate,
                         db: Session = Depends(get_db)):
    return datasets_crud.update_dataset_entry(db=db, dataset_entry_id=dataset_entry_id, dataset_entry_in=dataset_entry_data)


@router.delete('/entries/{dataset_entry_id}', tags=['datasets'], response_model=dataset_schema.DatasetEntry)
def delete_dataset_entry(dataset_entry_ud: str, db: Session = Depends(get_db)):
    return datasets_crud.delete_dataset_entry_by_id(db=db, dataset_entry_id=dataset_entry_ud)