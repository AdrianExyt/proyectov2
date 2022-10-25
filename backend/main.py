import json
import os
from typing import Union
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.cloud import datastore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./creds.json"
datastore_client = datastore.Client()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/form")
async def read_form(info: Request):
    req_info = await info.json()

    print(req_info["textInputName"])

    key = datastore_client.key("UserData")
    entity = datastore.Entity(key)
    entity.update({
        "textInputName": req_info["textInputName"],
        "textInputSurname": req_info["textInputSurname"],
        "emailInput": req_info["emailInput"],
        "passwordInput": req_info["passwordInput"],
        "countryInput": req_info["countryInput"]
    })

    datastore_client.put(entity)

    return {
        "status": "succes",
        "data": req_info
    }


@app.get("/query")
def fetch_data():
    query_data = datastore_client.query(kind='UserData')
    data = query_data.fetch()

    dataJsonInput: dict
    count = 0

    result = []

    for x in data:
        result.append({"textInputName": x['textInputName'], "passwordInput": x['passwordInput']})
    print(result)

    return result

@app.get("/query/{filter_str}")
def fetch_filter_data(filter_str):

    query_data = datastore_client.query(kind='UserData')
    print(filter_str)
    query_data.add_filter("textInputName", "=", filter_str)
    data = query_data.fetch()

    dataJsonInput: dict
    count = 0

    result = []

    for x in data:
        result.append({"textInputName": x['textInputName'], "passwordInput": x['passwordInput']})
    print(result)

    return result