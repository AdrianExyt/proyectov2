from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataForm(BaseModel):
    model: str
    textInputName: str
    textInputSurname: str
    emailInput: str
    passwordInput: str
    countryInput: str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/form")
def read_form(dataForm: DataForm):
    print("AAAAAAAAAAAAAAAAAAAAAAAAA")
    print(dataForm)
    return {"status": "succes"}
