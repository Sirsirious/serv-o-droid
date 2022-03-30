
from app.endpoints import conversations_router, intents_router
from app.endpoints import nlu_models_router
from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.database.database import Base, SessionLocal, engine
from app.database.models import conversations_models
from app.database.schemas import conversations_schemas
import sqlalchemy

###
# Database Setup
#

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


###
# App Setup
#

app = FastAPI()
app.include_router(conversations_router.router)
app.include_router(intents_router.router)
app.include_router(nlu_models_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
