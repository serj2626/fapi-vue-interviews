from tasks import send_email_for_verification_task
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import settings
from interviews import router as interviews_router
from users import router as users_router


app = FastAPI(
    title=settings.app.title,
    description=settings.app.description,
    version=settings.app.version,
)
app.include_router(users_router, prefix="/api/users")
app.include_router(interviews_router, prefix="/api/interviews")




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "OPTIONS",
    ],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Cookie",
        "X-CSRFToken",
        'Access-Control-Allow-Credentials',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Methods',
        'Access-Control-Allow-Origin',
        'Access-Authorization',
        "Authorization",
        "Bearer",
        'Access-Control-Allow-Origin'
    ],
)

@app.get("/")
async def root():
    send_email_for_verification_task.delay('serj2626@mail.ru')
    return {"message": "Письмо отправлено"}


@app.get("/hello")
async def root():
    return {"message": "Hello"}