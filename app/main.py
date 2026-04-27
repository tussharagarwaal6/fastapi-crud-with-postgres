from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi_pagination import add_pagination
from app.routers.v1.user import router as user_router
from app.routers.v1.task import router as task_router

#lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)
app.include_router(task_router)
add_pagination(app)

@app.get("/")
def ping():
    return {"message": "pong"}