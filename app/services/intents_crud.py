from sqlalchemy.orm import Session

# Intents
from app.database.models import intents_models
from app.database.schemas import intents_schemas


def get_intent(db: Session, intent_id: str):
    return db.query(intents_models.Intent). \
        filter(intents_models.Intent.id == intent_id).first()


def get_intent_by_name(db: Session, name: str):
    return db.query(intents_models.Intent). \
        filter(intents_models.Intent.name == name).first()


def get_intents(db: Session, limit: int = None):
    if not limit:
        return db.query(intents_models.Intent).all()
    else:
        return db.query(intents_models.Intent).limit(limit)


def update_intent(db: Session, intent: intents_schemas.IntentUpdate, intent_id: str):
    db_intent = db.query(intents_models.Intent). \
        filter(intents_models.Intent.id == intent_id).first()
    if db_intent:
        db_intent.update(intent.dict())
        db.commit()
        db.refresh(db_intent)
        return db_intent
    return None


def create_intent(db: Session, intent: intents_schemas.IntentCreate):
    db_intent = intents_models.Intent(**intent.dict())
    db.add(db_intent)
    db.commit()
    db.refresh(db_intent)
    return db_intent


def add_intent_to_intent_set(db: Session, intent_id: str, intent_set_id: str):
    db_intent_set = db.query(intents_models.IntentSet). \
        filter(intents_models.IntentSet.id == intent_set_id).first()
    if db_intent_set:
        db_intent = db.query(intents_models.Intent). \
            filter(intents_models.Intent.id == intent_id).first()
        if not db_intent:
            return None
        db_intent.intent_id = db_intent_set.id
        db.commit()
        db.refresh(db_intent)
        return db_intent
    return None


# IntentSets
def get_intent_set(db: Session, intent_set_id: str):
    return db.query(intents_models.IntentSet). \
        filter(intents_models.IntentSet.id == intent_set_id).first()


def get_intent_sets(db: Session, limit: int = None):
    if not limit:
        return db.query(intents_models.IntentSet).all()
    else:
        return db.query(intents_models.IntentSet).limit(limit)


def update_intent_set(db: Session, intent_set: intents_schemas.IntentSetUpdate, intent_set_id: str):
    db_intent_set = db.query(intents_models.IntentSet). \
        filter(intents_models.IntentSet.id == intent_set_id).first()
    if db_intent_set:
        db_intent_set.update(intent_set.dict())
        db.commit()
        db.refresh(db_intent_set)
        return db_intent_set
    return None


def create_intent_set(db: Session, intent_set: intents_schemas.IntentSetCreate):
    db_intent_set = intents_models.IntentSet(**intent_set.dict())
    db.add(db_intent_set)
    db.commit()
    db.refresh(db_intent_set)
    return db_intent_set
