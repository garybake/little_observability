import os

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI()


@app.get("/")
def read_root():
    return {"This": "TODO"}


@app.get("/version")
def read_version():
    vers = os.getenv('HUB_VERSION')
    return {"version": vers}
