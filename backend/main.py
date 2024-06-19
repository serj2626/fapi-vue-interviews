from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.config import settings
from interviews import router as interviews_router
from users import router as users_router
from users.tasks import send_email_verification

app = FastAPI(
    title=settings.app.title,
    description=settings.app.description,
    version=settings.app.version,
)
app.include_router(users_router, prefix="/api/users")
app.include_router(interviews_router, prefix="/api/interviews")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    send_email_verification.delay("serj", "serj2626@mail.ru")
    return {"message": "Письмо отправлено"}
