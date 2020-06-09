from typing import List, Dict

from pydantic import BaseModel


class RequestData(BaseModel):
    id: str
    data: List = None


class RequestItems(BaseModel):
    items: List[RequestData] = None


class ResponseData(BaseModel):
    id: str
    prediction : str
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


class ModelBean:
    status = "ACTIVE"
    def __init__(self, tenant, model_name, version, model_info):
        self.tenant = tenant
        self.model_name = model_name
        self.version = version
        self.model_info = model_info

    def to_string(self):
        print("tenant : {} \n model : {} \n version : {} \n status : {} \n info : {} "
              .format(self.tenant,self.model_name,self.version,self.status,self.model_info))

    def __eq__(self, obj):
        return isinstance(obj, ModelBean) \
               and obj.tenant == self.tenant \
               and obj.model_name == self.model_name  \
               and obj.version == self.version \
               and obj.status == self.status

    def __hash__(self):
        return hash(self.tenant)+hash(self.model_name)+hash(self.version)+hash(self.status)

