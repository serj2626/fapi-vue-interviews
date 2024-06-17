from fastapi import APIRouter

router = APIRouter(tags=["Пользователи && Авторизация"])


@router.get("/")
async def get_users():
    return {"message": "Hello World"}

@router.post("/signup")
async def signup():
    return {"message": "Signup successful"}

@router.post("/login")
async def login():
    return {"message": "Login successful"}