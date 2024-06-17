from fastapi import APIRouter

router = APIRouter(prefix='/interviews', tags=['Собеседования'])


@router.get("/")
async def get_users():
    return {"message": "Hello World"}