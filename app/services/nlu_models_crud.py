from datetime import datetime

from sqlalchemy.orm import Session

# NLU
from app.database.models import nlu_model_registry_models
from app.database.schemas import nlu_model_registry_schema
from app.settings import MODEL_DIRECTORY


def get_nlu_models(db: Session):
    return db.query(nlu_model_registry_models.NLUModel).all()


def get_nlu_model(db: Session, nlu_model_id: str):
    return db.query(nlu_model_registry_models.NLUModel) \
        .filter(nlu_model_registry_models.NLUModel.id == nlu_model_id).first()


def update_nlu_model(db: Session, nlu_model_id: str,
                     nlu_model: nlu_model_registry_schema.NLUModelSchemaUpdate):
    db_nlu_model = db.query(nlu_model_registry_models.NLUModel) \
        .filter(nlu_model_registry_models.NLUModel.id == nlu_model_id).first()
    if db_nlu_model:
        db_nlu_model.update(nlu_model.dict())
        db.commit()
        db.refresh(db_nlu_model
                   )
        return db_nlu_model
    return None


def create_nlu_model(db: Session, nlu_model: nlu_model_registry_schema.NLUModelSchemaCreate):
    db_nlu_model = nlu_model_registry_models.NLUModel(**nlu_model.dict())
    db.add(db_nlu_model)
    db.commit()
    db.refresh(db_nlu_model)
    return db_nlu_model


def update_last_trained_at(db: Session, last_trained_at: datetime, nlu_model_id: str):
    db_nlu_model = db.query(nlu_model_registry_models.NLUModel) \
        .filter(nlu_model_registry_models.NLUModel.id == nlu_model_id).first()
    if db_nlu_model:
        db_nlu_model.last_trained_at = last_trained_at
        db.commit()
        db.refresh(db_nlu_model)
        return db_nlu_model
    return None


def delete_nlu_model(db: Session, nlu_model_id: str):
    db_nlu_model = db.query(nlu_model_registry_models.NLUModel) \
        .filter(nlu_model_registry_models.NLUModel.id == nlu_model_id).first()
    if db_nlu_model:
        db.delete(db_nlu_model)
        db.commit()
        return db_nlu_model
    return None


def get_training_results_by_model(db: Session, nlu_model_id: str):
    return db.query(nlu_model_registry_models.TrainingResult) \
        .filter(nlu_model_registry_models.TrainingResult.nlu_model_id == nlu_model_id).all()


def get_training_result(db: Session, training_result_id: str):
    return db.query(nlu_model_registry_models.TrainingResult) \
        .filter(nlu_model_registry_models.TrainingResult.id == training_result_id).first()


def add_training_result(db: Session, training_result: nlu_model_registry_schema.TrainingResultSchemaCreate):
    db_training_result = nlu_model_registry_models.TrainingResult(**training_result.dict())
    db.add(db_training_result)
    db.commit()
    db.refresh(db_training_result)
    return db_training_result


def update_training_result(db: Session, training_result_id: str,
                           training_result: nlu_model_registry_schema.TrainingResultSchemaUpdate):
    db_training_result = db.query(nlu_model_registry_models.TrainingResult) \
        .filter(nlu_model_registry_models.TrainingResult.id == training_result_id).first()
    if db_training_result:
        db_training_result.update(training_result.dict())
        db.commit()
        db.refresh(db_training_result)
        return db_training_result
    return None


def delete_training_result(db: Session, training_result_id: str):
    db_training_result = db.query(nlu_model_registry_models.TrainingResult) \
        .filter(nlu_model_registry_models.TrainingResult.id == training_result_id).first()
    if db_training_result:
        db.delete(db_training_result)
        db.commit()
        return db_training_result
    return None
