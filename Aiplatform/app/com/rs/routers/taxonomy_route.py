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
    count : int = None

class ConfigRequestData(BaseModel):
    tenant: str
    algo : str
    config_status: str
    model_root_path : str
    version : str
    preprocess : List[str]
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


@app.post("/productTaxonomy/real/predict", response_model=ResponseItems)
def real_time_predict(item: RequestItems):
    try:
        # Extract model in correct order
        item = ResponseItems(items=[ResponseData(id='123', prediction="1", additional_parameter={"confidence": "90"})] , count=1)

        print("my input {}".format(item.json()))
        return item.dict()
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}


@app.post("/productTaxonomy/batch/predict", response_model=ResponseItems)
async def batch_predict(item: RequestItems):
    try:
        # Extract model in correct order
        print("my input {}".format(item.json()))
        item = ResponseItems(items=[ResponseData(id='123', prediction='1', additional_parameter={"confidence": "90"})] )
        return item.dict()
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}


@app.get("/productTaxonomy/config/{tenant}", response_model=ConfigRequestData)
def get_config(tenant):
    cache = CacheFactory.getInstance().get_cache_type()
    if cache.get(tenant) is None:
        raise KeyNotFoundException(name=tenant, code = 404)

    return cache.get(tenant)

@app.post("/productTaxonomy/config", response_model=ConfigRequestData , status_code=status.HTTP_201_CREATED)
def update_config(tenant_config : ConfigRequestData):
    '''
    :param tenant_config:
    :return: Configuration required to setup product taxonomy classification.
    '''
    # config = {"tenant": "1",
    #           "algo": "product_taxonomy",
    #           "config_status": "complete",
    #           "model_root_path": "fs/as/as/model",
    #           "version": "v1",
    #           "preprocess": ["preprocess_1.pkl", "preprocess_2.pkl"],
    #           "postprocess": ["postprocess_1.py", "prostprocess.py"],
    #           "model_file": ["model.pkl"]}

    cache = CacheFactory.getInstance().get_cache_type()
    cache.update(tenant_config.tenant, tenant_config.dict())
    myte = cache.get(tenant_config.tenant)
    return myte
