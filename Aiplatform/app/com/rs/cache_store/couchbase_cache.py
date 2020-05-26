from __future__ import annotations

from typing import Optional

from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

from Aiplatform.app.com.rs.config.load_config import ConfigReader


class CouchBaseCacheMeta(type):
    _instance: Optional[CouchBaseCache] = None
    _cluster: Cluster = None

    def __call__(self) -> CouchBaseCache:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class CouchBaseCache(metaclass=CouchBaseCacheMeta):

    def initialize(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
    config = ConfigReader.getInstance().config
    print("initialize the Couchbase --> {}".format(dict(config)))
    host = config.get("cache.couchbase", 'host')
    user = config.get("cache.couchbase", 'user')
    passwd = config.get("cache.couchbase", 'passwd')

    ##super._cluster = Cluster('couchbase://' + host, ClusterOptions(PasswordAuthenticator(user, passwd)))
