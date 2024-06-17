from fastapi import FastAPI

from interviews import router as interviews_router
from users import router as users_router

app = FastAPI()
app.include_router(users_router, prefix="/api/users")
app.include_router(interviews_router, prefix="/api/interviews")


@app.get("/")
async def root():
    return {"message": "Hello World"}
