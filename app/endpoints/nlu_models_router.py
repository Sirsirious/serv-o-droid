from typing import Optional, List

from fastapi import APIRouter, Depends
from requests import Session

from app.database.database import get_db
from app.database.schemas import nlu_model_registry_schema
from app.services import nlu_models_crud

router = APIRouter(prefix='/nlu_models')


@router.get('/', tags=['nlu_models'], response_model=List[nlu_model_registry_schema.NLUModelSchema])
async def list_models(db: Session = Depends(get_db)):
    return nlu_models_crud.get_nlu_models(db=db)


@router.get('/{model_id}', tags=['nlu_models'], response_model=nlu_model_registry_schema.NLUModelSchema)
async def get_model_id_metadata(nlu_model_id: str, db: Session = Depends(get_db)):
    return nlu_models_crud.get_nlu_model(db=db, nlu_model_id=nlu_model_id)


@router.post('/', tags=['nlu_models'], response_model=nlu_model_registry_schema.NLUModelSchema)
async def create_model(model: nlu_model_registry_schema.NLUModelSchemaCreate, db: Session = Depends(get_db)):
    return nlu_models_crud.create_nlu_model(db=db, nlu_model=model)


@router.patch('/{model_id}', tags=['nlu_models'], response_model=nlu_model_registry_schema.NLUModelSchema)
async def update_model(nlu_model_id: str, update_model_schema: nlu_model_registry_schema.NLUModelSchemaUpdate,
                       db: Session = Depends(get_db)):
    return nlu_models_crud.update_nlu_model(db=db, nlu_model_id=nlu_model_id, nlu_model=update_model_schema)


@router.put('/{model_id}', tags=['nlu_models'])
async def promote_model(model_id: str):
    return f'model {model_id} promoted'


@router.delete('/{model_id}', tags=['nlu_models'])
async def delete_model(nlu_model_id: str, db: Session = Depends(get_db)):
    return nlu_models_crud.delete_nlu_model(db=db, nlu_model_id=nlu_model_id)


### Training Results ###

@router.get('/{model_id}/training_results', tags=['nlu_models'],
            response_model=List[nlu_model_registry_schema.TrainingResultSchema])
async def get_model_training_results(nlu_model_id: str, db: Session = Depends(get_db)):
    return nlu_models_crud.get_training_results_by_model(db=db, nlu_model_id=nlu_model_id)


@router.get('/training_result/{training_result_id}', tags=['nlu_models'],
            response_model=nlu_model_registry_schema.TrainingResultSchema)
async def get_training_result(training_result_id: str, db: Session = Depends(get_db)):
    return nlu_models_crud.get_training_result(db=db, training_result_id=training_result_id)


@router.post('/train', tags=['nlu_models'], response_model=nlu_model_registry_schema.TrainingResultSchema)
async def train_model(training_result_data: nlu_model_registry_schema.TrainingResultSchemaCreate,
                      db: Session = Depends(get_db)):
    return nlu_models_crud.add_training_result(db=db, training_result=training_result_data)


@router.put('/training_results/{training_result_id}', tags=['nlu_models'])
async def update_training_result(training_result_id: str,
                                 training_result_update_data: nlu_model_registry_schema.TrainingResultSchemaUpdate,
                                 db: Session = Depends(get_db)):
    return nlu_models_crud.update_training_result(db=db, training_result_id=training_result_id,
                                                  training_result=training_result_update_data)


@router.delete('/training_results/{training_result_id}', tags=['nlu_models'])
async def delete_training_result(training_result_id: str, db: Session = Depends(get_db)):
    return nlu_models_crud.delete_training_result(db=db, training_result_id=training_result_id)
