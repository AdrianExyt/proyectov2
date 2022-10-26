import base64
import json
import os
from typing import Any, Union
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.cloud import datastore, storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./creds.json"
datastore_client = datastore.Client()
storage_client = storage.Client()


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

@app.post("/img")
def upload_blob(thumbnail: UploadFile = File(...)):
    print("THUMBNAAAAIL")
    print(thumbnail)

    bucket = storage_client.bucket("proyectov2storage")
    blob = bucket.blob(thumbnail.filename)
    print("FILEEEE")
    print(thumbnail.file)
    fileBytes = base64.b64encode(thumbnail.file)
    print("BYTEEEEES")
    print(fileBytes)
    return blob.upload_from_filename(thumbnail)