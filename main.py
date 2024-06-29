from fastapi import FastAPI
from app.api.v1.endpoints import merchant_data as merchant_data_v1
from app.db.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(merchant_data_v1.router, prefix="/api/v1/merchant_data", tags=["merchant_data"])

@app.get("/")
def read_root():
    return {"message": "Hello World"}
