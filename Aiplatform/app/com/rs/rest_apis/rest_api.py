# Data Handling
import logging
import pickle
from typing import List, Dict

import numpy as np
from pydantic import BaseModel

# Server
import uvicorn
from fastapi import FastAPI

# Modeling
import lightgbm

from Aiplatform.app.com.rs.cache_store.distributed_cache import read_config, open_cache_collection

app = FastAPI()



# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)


# logging.basicConfig(level=logging.DEBUG, filename='sample.log')

# Initialize files


class RequestData(BaseModel):
    id: str
    data: Dict[str, str] = None


class RequestItems(BaseModel):
    items: List[RequestData] = None


class ResponseData(BaseModel):
    id: str
    prediction: str
    additional_parameter: Dict[str, str] = None


class ResponseItems(BaseModel):
    items: List[ResponseData] = None


class HeartbeatResponse(BaseModel):
    heart_beat: str


@app.on_event("startup")
async def startup_event():



    config = read_config()
    ac_cache=open_cache_collection(config.get('cb','host'),config.get('cb','user'),
                          config.get('cb','pass'),config.get('autoClass','bucket'))




@app.post("/predict", response_model=ResponseItems)
def predict(item: RequestItems):
    try:
        # Extract model in correct order
        print("my input {}".format(item.json()))

        item = ResponseItems(items=[ResponseData(id='123', prediction='1')])

        return item.dict()

    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}


@app.get("/", response_model=HeartbeatResponse)
def heart_beat():
    hb = HeartbeatResponse(heart_beat={"heart_beat": "I am good "})
    return hb.dict()
