import base64
from cmath import log
from http import client
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
last_id: str


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
    global last_id
    req_info = await info.json()

    key = datastore_client.key("UserData")
    entity = datastore.Entity(key)
    entity.update({
        "textInputName": req_info["textInputName"],
        "textInputSurname": req_info["textInputSurname"],
        "emailInput": req_info["emailInput"],
        "passwordInput": req_info["passwordInput"],
        "countryInput": req_info["countryInput"],
        "imgStored": req_info["imgStored"]
    })

    datastore_client.put(entity)
    last_id = entity.id
    print(last_id)

    return {
        "status": "succes",
        "data": req_info
    }


@app.get("/query")
def fetch_data():
    query_data = datastore_client.query(kind='UserData')
    data = query_data.fetch()

    result = []

    for x in data:
        result.append({"textInputName": x['textInputName'], "passwordInput": x['passwordInput'], "id": x.id, "imgStored":x['imgStored']})
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
        result.append({"textInputName": x['textInputName'], "passwordInput": x['passwordInput'], "id": x.id, "imgStored":x['imgStored']})
    print(result)

    return result

@app.post("/img")
def upload_blob(thumbnail: UploadFile = File(...)):
    print(thumbnail)

    bucket = storage_client.bucket("proyectov2img")
    print(last_id)
    blob = bucket.blob(str(last_id) + ".jpg")
    
    return blob.upload_from_file(thumbnail.file)

@app.get("/edit/{id}")
def get_id(id):
    print("IIIIIIIIIIIIIIIIIDDDDDDDDDDDDD")
    print(id)
    first_key = datastore_client.key("UserData", int(id))
    task = datastore_client.get(first_key)
    print(task)
    return task

@app.put("edit/{id}")
async def put_id(id, info: Request):

    req_info = await info.json()

    with datastore_client.transaction():
        first_key = datastore_client.key("UserData", int(id))
        task = datastore_client.get(first_key)

        task["textInputName"] = req_info["textInputName"]
        task["textInputSurname"] = req_info["textInputSurname"]
        task["emailInput"] = req_info["emailInput"]
        task["passwordInput"] = req_info["passwordInput"]
        task["countryInput"] = req_info["countryInput"]
        task["imgStored"] = req_info["imgStored"]