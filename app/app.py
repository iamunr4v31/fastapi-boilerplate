from fastapi import FastAPI
from app.router.controller import router
from utils import create_db_and_tables, get_session

app: FastAPI = FastAPI()
app.include_router(router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello User"}