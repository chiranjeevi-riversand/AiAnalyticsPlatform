# Data Handling
import logging
from typing import List, Dict

# Server
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette import status

from Aiplatform.app.com.rs.cache_store.cache_factory import CacheFactory
# Modeling
from Aiplatform.app.com.rs.config.load_config import ConfigReader
from Aiplatform.app.com.rs.exception.keynotfoundexception import KeyNotFoundException
from Aiplatform.app.com.rs.services.config_manager import ConfigManager

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
    count: int = None


class ConfigRequestData(BaseModel):
    tenant: str
    version: str
    model_name: str = "productTaxonomy"
    model_blob_path: str
    preprocess: List[str]
    postprocess: List[str]
    model_file: List[str]


@app.exception_handler(KeyNotFoundException)
async def key_not_found_exception_handler(request: Request, exc: KeyNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! tenant setup : {exc.name} not found .."}
    )


@app.on_event("startup")
async def startup_event():
    ConfigReader.getInstance()
    CacheFactory.getInstance()


@app.post("/api/{tenant}/productTaxonomy/{version}/real/predict", response_model=ResponseItems)
def real_time_predict(item: RequestItems):
    try:
        # Extract model in correct order
        item = ResponseItems(items=[ResponseData(id='123', prediction="1", additional_parameter={"confidence": "90"})],
                             count=1)

        print("my input {}".format(item.json()))
        return item.dict()
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}


@app.post("/api/{tenant}/productTaxonomy/{version}/batch/predict", response_model=ResponseItems)
async def batch_predict(item: RequestItems):
    try:

        print("my input {}".format(item.json()))
        item = ResponseItems(items=[ResponseData(id='123', prediction='1', additional_parameter={"confidence": "90"})])




        return item.dict()
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}


@app.get("/api/{tenant}/productTaxonomy/config", response_model=ConfigRequestData)
def get_config(tenant):

    conf = ConfigManager.get_config(tenant)
    if conf is None:
        raise KeyNotFoundException(name=tenant, code=404)

    return conf


@app.post("api/{tenant}/productTaxonomy/config", response_model=ConfigRequestData, status_code=status.HTTP_201_CREATED)
def update_config(tenant_config: ConfigRequestData):
    '''
    :param tenant_config:
    :return: Configuration required to setup product taxonomy classification.
    '''
    ConfigManager.save_config(tenant_config)
    myte = ConfigManager.get_config(tenant_config)
    return myte
