from fastapi import APIRouter

from app.model.schemas import CreateModelSchema
from app.model.service import ModelService

router = APIRouter(
    prefix='/model',
    tags=['model'],
)

@router.get('/')
async def get_model():
    return { 'hola': 'hola' }

@router.post('/')
async def create_model(model: CreateModelSchema):
    return ModelService.calcule_turbiedad(model=model)
