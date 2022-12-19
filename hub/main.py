import os

from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
prefix_router = APIRouter(prefix=f"/{os.getenv('HUB_API_VERSION')}")


@prefix_router.get("/")
def read_root():
    return {"This": "TODO"}


@app.get("/version")
def read_version():
    vers = os.getenv('HUB_VERSION')
    return {"version": vers}


@prefix_router.get("/consumption")
def read_consumption():
    return {"consumption": 10.1}


app.include_router(prefix_router)
