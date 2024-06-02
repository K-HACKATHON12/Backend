from fastapi import FastAPI
from app.api.v1.endpoints import example as example_v1

app = FastAPI()

app.include_router(example_v1.router, prefix="/api/v1/example", tags=["example_v1"])

@app.get("/")
def read_root():
    return {"message": "Hello World"}
