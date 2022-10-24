from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/form")
def read_form(data):
    print("AAAAAAAAAAAAAAAAAAAAAAAAA")
    print(data)
    return {}
