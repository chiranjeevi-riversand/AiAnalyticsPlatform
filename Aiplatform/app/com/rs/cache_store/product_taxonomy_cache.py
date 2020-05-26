import datetime
import pickle
import random

from Aiplatform.app.com.rs.cache_store.interface_file_cache import ICache


class ProductTaxonomyCache(ICache):

    def __init__(self,file_path):
        super().__init__()
        self.read_from_fs_update_cache(file_path)

    def read_from_fs_update_cache(self,file_path:str):
        clf = pickle.load(open(file_path + '\\model.pickle', 'rb'))
        enc = pickle.load(open(file_path + '\\encoder.pickle', 'rb'))
        features = pickle.load(open(file_path + '\\features.pickle', 'rb'))

        self.update("classifier",clf)
        self.update("onehotencoder", enc)
        self.update("features", features)

