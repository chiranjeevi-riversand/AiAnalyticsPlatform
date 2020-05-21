import os
from configparser import ConfigParser

import couchbase
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.collection import CBCollection
from couchbase_core.cluster import PasswordAuthenticator
from couchbase.exceptions import *
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

from Aiplatform.app.com.rs.exception.key_not_found_exception import KeyNotFoundException

file_path = "D:\\Projects\\AiAnalyticPlatform\\Aiplatform\\app\\model"

def open_cache_collection(host, user, passwd, bucket_name):
    cluster = Cluster('couchbase://'+host, ClusterOptions(PasswordAuthenticator(user, passwd)))
    bucket = cluster.bucket(bucket_name)
    coll = bucket.default_collection()
    return coll

def load_ac_model_to_cache(collection:CBCollection):

    clf = pickle.load(open(file_path + '\\model.pickle', 'rb'))
    enc = pickle.load(open(file_path + '\\encoder.pickle', 'rb'))
    features = pickle.load(open(file_path + '\\features.pickle', 'rb'))

    collection.upsert


# a simple function to read an array of configuration files into a config object
def read_config(cfg_files="app_config.properties"):
    if cfg_files is not None:
        config = ConfigParser.RawConfigParser()

        # merges all files into a single config
        for i, cfg_file in enumerate(cfg_files):
            if os.path.exists(os.path.join("./../../../", cfg_file)):
                config.read(cfg_file)
        return config

# def getFromFileSystem(key):
#     v = None
#     with open("./../../../../app_config.properties", mode='r') as f:
#         for line in f:
#             k,v = line.split('\t')
#             if k == key:
#                 return json.loads(v[:-1])
#     raise KeyNotFoundException("Key not present in permanent storage")
