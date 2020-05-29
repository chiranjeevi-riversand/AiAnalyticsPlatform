import datetime
import pickle
import random

from Aiplatform.app.com.rs.cache_store.interface_file_cache import ICache
from Aiplatform.app.com.rs.config.load_config import ConfigReader


class ProductTaxonomyCache(ICache):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ProductTaxonomyCache.__instance is None:
            ProductTaxonomyCache()
        return ProductTaxonomyCache.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ProductTaxonomyCache.__instance != None:
            pass
        else:
            # system_config = ConfigReader.getInstance().config
            # cache_type = system_config.get("cache.enabled", "cache")
            # model_path = system_config.get(cache_type, "file.path")
            # print("initializing singleton class ---> ProductTaxonomyCache {} {}".format(cache_type,model_path))

            super().__init__()
            ProductTaxonomyCache.__instance = self
            #self.__load_cache(model_path)


    # def __load_cache(self, file_path: str):
    #     clf = pickle.load(open(file_path + '\\model.pickle', 'rb'))
    #     enc = pickle.load(open(file_path + '\\encoder.pickle', 'rb'))
    #     features = pickle.load(open(file_path + '\\features.pickle', 'rb'))
    #
    #     self.update("classifier", clf)
    #     self.update("onehotencoder", enc)
    #     self.update("features", features)
