from typing import Optional

from fastapi import APIRouter

router = APIRouter(prefix='/nlu_models')


@router.get('/', tags=['nlu_models'])
async def list_models():
    return []


@router.get('/{model_id}', tags=['nlu_models'])
async def get_model_id_metadata(model_id: int, q: Optional[str] = None):
    return {"model": "foo"}


@router.post('/', tags=['nlu_models'])
async def create_model():
    return 'new_model'


@router.patch('/{model_id}', tags=['nlu_models'])
async def update_model(model_id: int, q: Optional[str] = None):
    return 'updated model'


@router.put('/{model_id}', tags=['nlu_models'])
async def promote_model(model_id: int, q: Optional[str] = None):
    return f'model {model_id} promoted'