from fastapi import APIRouter

router = APIRouter(prefix="auth", tags=["Пользователи && Авторизация"])


@router.get("/users")
async def get_users():
    return {"message": "Hello World"}