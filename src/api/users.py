from typing import Annotated
from fastapi import APIRouter, Depends, status

from api.dependencies import model_service
from schemas.users import UserInfo
from services.model import ModelService
from utils.error_handler import handle_route_error


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('', status_code=status.HTTP_200_OK)
async def add_user(
    user_info: UserInfo,
    service: Annotated[ModelService, Depends(model_service)],
):
    try:
        predict = await service.predict(user_info)
        return predict
    
    except Exception as e:
        await handle_route_error(e, status_code=status.HTTP_400_BAD_REQUEST)
