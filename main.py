from typing import Union

from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{json_file}")
def read_assetlinks(json_file: str):
    with open(json_file) as f:
        return json.load(f)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}