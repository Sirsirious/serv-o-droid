import logging
import os
from os.path import dirname, join
from pathlib import Path

from fastapi import FastAPI

from app.database.database import Base, SessionLocal, engine
from app.endpoints import (
    conversations_router,
    intents_router,
    datasets_router,
    nlu_models_router)


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
# Model folder setup
#

ML_MODELS_FOLDER = join(dirname(__file__), 'ml_models')
if not os.path.exists(ML_MODELS_FOLDER):
    os.mkdir(ML_MODELS_FOLDER)

###
# Setup Logger
#
logs_target = Path(dirname(__file__)).parent.absolute().joinpath('logs')
if not os.path.exists(logs_target):
    os.mkdir(logs_target)
if not os.path.exists(logs_target.joinpath("servodroid.log")):
    open(logs_target.joinpath("servodroid.log"), "w+")
logger = logging.getLogger("servodroid-logger")
logging.basicConfig(filename=logs_target.joinpath("servodroid.log"), level=logging.DEBUG)

###
# App Setup
#

logger.info("Starting Servo-droid")
logger.info("Loading routes")
app = FastAPI()
app.include_router(conversations_router.router)
app.include_router(intents_router.router)
app.include_router(datasets_router.router)
app.include_router(nlu_models_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
