import os
import pickle
from typing import List

from Aiplatform.app.com.rs.bean import ModelBean
from Aiplatform.app.com.rs.cache_store.interface_file_cache import ICache
from Aiplatform.app.com.rs.config.load_config import ConfigReader


class ProductTaxonomyCache(ICache):
    __instance = None
    __algo = "product_taxonomy"
    __algo_info_config: List = ConfigReader.getInstance().get_algo_config_info_details()

    #__tenant_info = ConfigReader.getInstance().get_tenant_config_info()

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
            super().__init__()
            ProductTaxonomyCache.__instance = self

    def get_algo_info(self, tenant, version):
        mb = ModelBean(tenant, self.__algo, version)
        model_info = next((x for x in self.__algo_info_config if x.value == mb), None)
        print(model_info)

        predictor_class = model_info.get("class")
        model_path = model_info.get("modelPath")
        predictor_pkl = model_info.get("predictor").get("object")
        preprocess_pkl = model_info.get("preprocess").get("object")

        print(predictor_pkl, predictor_class, preprocess_pkl, model_path)

        preprocessor_path = os.path.join(model_path, preprocess_pkl)
        predictor_path = os.path.join(model_path, predictor_pkl)


        with open(preprocessor_path, 'rb') as f:
            preprocessor = pickle.load(f)

        with open(predictor_path, 'rb') as f:
            predictor = pickle.load(f)

        self.update("info", model_info)
        self.update("preprocessor", preprocessor)
        self.update("predictor", predictor)

        return model_info


    def get_model_key(self,suffix):
        return "PT_"+suffix
