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