from Aiplatform.app.com.rs.cache_store.cache_factory import CacheFactory


class CacheServiceManager:

    def __init__(self):
        pass

    @staticmethod
    def save_config( config_req_object):
        CacheFactory.getInstance().get_cache_type().update(config_req_object.tenant, config_req_object.dict())

    @staticmethod
    def get_config(config_req_object):
        CacheFactory.getInstance().get_cache_type().get(config_req_object)