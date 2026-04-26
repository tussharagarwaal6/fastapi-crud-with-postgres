from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers.v1.user import router as user_router

#lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)

@app.get("/")
def ping():
    return {"message": "pong"}