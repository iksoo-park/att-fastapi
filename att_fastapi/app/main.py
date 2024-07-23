from fastapi import FastAPI
from typing import Optional

from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

app.include_router(exponentialRegressionRouter)