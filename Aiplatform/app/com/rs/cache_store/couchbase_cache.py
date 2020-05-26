import os
from configparser import ConfigParser

from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

from Aiplatform.app.com.rs.cache_store.interface_file_cache import ICache


class CouchBaseCache(ICache):
    file_path = "D:\\Projects\\AiAnalyticPlatform\\Aiplatform\\app\\model"

    def __init__(self):
        config = self.read_config()
        self.cluster = self.open_cache_collection(config.get('cb', 'host'), config.get('cb', 'user'),
                                                  config.get('cb', 'pass'), config.get('autoClass', 'bucket'))

    def open_cache_collection(self, host, user, passwd):
        Cluster('couchbase://' + host, ClusterOptions(PasswordAuthenticator(user, passwd)))

