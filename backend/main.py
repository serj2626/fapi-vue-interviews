from fastapi import FastAPI

from config import settings
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


@app.get("/")
async def root():
    send_email_verification.delay("serj", "serj@serj")
    return {"message": "Hello World"}
