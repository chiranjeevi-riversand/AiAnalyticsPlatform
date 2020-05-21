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

app = FastAPI()

file_path = "D:\\Projects\\AiAnalyticPlatform\\Aiplatform\\app\\model"

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, filename='sample.log')

# Initialize files
clf = pickle.load(open(file_path + '\\model.pickle', 'rb'))
enc = pickle.load(open(file_path + '\\encoder.pickle', 'rb'))
features = pickle.load(open(file_path + '\\features.pickle', 'rb'))


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
