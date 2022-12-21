import os

from fastapi import FastAPI
from dotenv import load_dotenv

from api import api_router

load_dotenv()


# Setup app
app = FastAPI()

# Setup routes
app.include_router(api_router, prefix=f"/api/{os.getenv('HUB_API_VERSION')}")


# Top level routes
# TODO move these
@app.get("/")
async def read_root():
    return {"This": "TODO"}


@app.get("/version")
async def read_version():
    vers = os.getenv('HUB_VERSION')
    return {"version": vers}
