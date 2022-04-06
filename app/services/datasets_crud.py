from sqlalchemy.orm import Session

from app.database.models import dataset_model
from app.database.schemas import dataset_schema


def get_dataset(db: Session, dataset_id: str):
    return db.query(dataset_model.Dataset).filter(dataset_model.Dataset.id == dataset_id).first()


def get_datasets(db: Session):
    return db.query(dataset_model.Dataset).all()


def update_dataset(db: Session, dataset_id: str, dataset_in: dataset_schema.DatasetUpdate):
    dataset = db.query(dataset_model.Dataset).filter(dataset_model.Dataset.id == dataset_id).first()

    if dataset:
        dataset.name = dataset_in.name
        dataset.description = dataset_in.description
        db.commit()
        return dataset_schema.Dataset(**dataset.to_dict())
    return None


def delete_dataset(db: Session, dataset_id: str):
    dataset = db.query(dataset_model.Dataset).filter(dataset_model.Dataset.id == dataset_id).first()

    if dataset:
        db.delete(dataset)
        db.commit()
        return dataset_schema.Dataset(**dataset.to_dict())
    return None


def create_dataset(db: Session, dataset_in: dataset_schema.DatasetCreate):
    dataset = dataset_model.Dataset(**dataset_in.dict())
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    return dataset_schema.Dataset(**dataset.to_dict())


def get_dataset_entries(db: Session, dataset_id: str):
    return db.query(dataset_model.DatasetEntry).filter(dataset_model.DatasetEntry.dataset_id == dataset_id).all()


def add_dataset_entry(db: Session, dataset_id: str, dataset_entry_in: dataset_schema.DatasetEntryCreate):
    dataset_entry = dataset_model.DatasetEntry(**dataset_entry_in.dict())
    dataset_entry.dataset_id = dataset_id
    db.add(dataset_entry)
    db.commit()
    db.refresh(dataset_entry)
    return dataset_schema.DatasetEntry(**dataset_entry.to_dict())


def get_dataset_entry_by_id(db: Session, dataset_entry_id: str):
    return db.query(dataset_model.DatasetEntry).filter(dataset_model.DatasetEntry.id == dataset_entry_id).first()


def update_dataset_entry(db: Session, dataset_entry_id: str, dataset_entry_in: dataset_schema.DatasetEntryUpdate):
    dataset_entry = db.query(dataset_model.DatasetEntry).filter(dataset_model.DatasetEntry.id == dataset_entry_id).first()

    if dataset_entry:
        dataset_entry.intent_id = dataset_entry_in.intent_id
        db.commit()
        return dataset_schema.DatasetEntry(**dataset_entry.to_dict())
    return None


def delete_dataset_entry_by_id(db: Session, dataset_entry_id: str):
    dataset_entry = db.query(dataset_model.DatasetEntry).filter(dataset_model.DatasetEntry.id == dataset_entry_id).first()

    if dataset_entry:
        db.delete(dataset_entry)
        db.commit()
        return dataset_schema.DatasetEntry(**dataset_entry.to_dict())
    return None