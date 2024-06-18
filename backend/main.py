from fastapi import FastAPI

from interviews import router as interviews_router
from users import router as users_router
from users.tasks import send_email_verification

app = FastAPI()
app.include_router(users_router, prefix="/api/users")
app.include_router(interviews_router, prefix="/api/interviews")


@app.get("/")
async def root():
    send_email_verification.delay("serj", "serj@serj")
    return {"message": "Hello World"}
