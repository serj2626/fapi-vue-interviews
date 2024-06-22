from fastapi import APIRouter, Depends
from .dependencies import create_interview


router = APIRouter(tags=["Собеседования"])


@router.get("/")
async def get_interviews():
    return {"message": "All interviews"}


@router.post('/')
async def create_interview(vacancy=Depends(create_interview)):
    return {"message": "Create interview", "data": vacancy}
