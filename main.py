from typing import Union

from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/.well-known/assetlinks.json")
def read_assetlinks():
    with open('.well-known/assetlinks.json') as f:
        return json.load(f)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}