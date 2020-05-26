from Aiplatform.app.com.rs.cache_store.couchbase_cache import CouchBaseCache
from Aiplatform.app.com.rs.cache_store.product_taxonomy_cache import ProductTaxonomyCache

file_path = "D:\\Projects\\AiAnalyticPlatform\\Aiplatform\\app\\model"


def load_cache_factory(cache_type : str):
    if cache_type is "local":
        return ProductTaxonomyCache(get_blob_path())
    elif cache_type is "couch":
        return CouchBaseCache()

def get_blob_path():
    return "D:\\Projects\\AiAnalyticPlatform\\Aiplatform\\app\\model"