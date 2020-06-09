# Data Handling
import logging
# Server
import traceback

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status

from Aiplatform.app.com.rs.bean import ResponseItems, ResponseData, ConfigRequestData, RequestItems
from Aiplatform.app.com.rs.cache_store.cache_factory import CacheFactory
from Aiplatform.app.com.rs.config.load_config import ConfigReader
from Aiplatform.app.com.rs.exception.raise_exception import KeyNotFoundException, InternalServerException
# Modeling
from Aiplatform.app.com.rs.services.cache_manager import CacheServiceManager
from Aiplatform.app.com.rs.services.tenant_config_manager import TenantConfigManager

app = FastAPI()

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)


logging.basicConfig(level=logging.DEBUG, filename='sample.log')

# Initialize files


@app.on_event("startup")
async def startup_event():
    ConfigReader.getInstance()
    CacheFactory.getInstance()
    pass


@app.post("/api/{tenant}/productTaxonomy/{version}/real/predict", response_model=ResponseItems)
def real_time_predict(tenant: str, version: str , items: RequestItems):
    try:
        print("input -->", items.dict())
        output = TenantConfigManager().tenant(tenant).version(version).model("product_taxonomy").extract(items).predict()

        lst = ([ResponseData(id=data.id, prediction=score) for data, score in zip(items.items, output)])

        a = ResponseItems(items=lst, count=lst.__len__())

        return a
    except Exception as err:
        traceback.print_exc()
        my_logger.exception(err)
        my_logger.error("Something went wrong!")
        raise InternalServerException(name=tenant, code=404)


@app.post("/api/{tenant}/productTaxonomy/{version}/batch/predict", response_model=ResponseItems)
async def batch_predict(tenant: str, version: str ,items: RequestItems):
    try:
        print("input -->", items.dict())
        output = TenantConfigManager().tenant(tenant).version(version).model("product_taxonomy").extract(
            items).predict()

        lst = ([ResponseData(id=data.id, prediction=score) for data, score in zip(items.items, output)])

        a = ResponseItems(items=lst, count=lst.__len__())

        return a
    except Exception as err:
        traceback.print_exc()
        my_logger.exception(err)
        my_logger.error("Something went wrong!")
        raise InternalServerException(name=tenant, code=404)


@app.get("/api/{tenant}/productTaxonomy/config")
def get_config(tenant):
    print(" -----> ", tenant)
    conf = TenantConfigManager().tenant(tenant).given_tenant_get_model_info()
    if conf is None:
        raise KeyNotFoundException(name=tenant, code=404)

    return conf


@app.post("/api/{tenant}/productTaxonomy/config", response_model=ConfigRequestData, status_code=status.HTTP_201_CREATED)
def update_config(tenant_config: ConfigRequestData):
    '''
    :param tenant_config:
    :return: Configuration required to setup product taxonomy classification.
    '''
    CacheServiceManager.save_config(tenant_config)
    myte = CacheServiceManager.get_config(tenant_config)
    return myte
