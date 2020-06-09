# a simple function to read an array of configuration files into a config object
import configparser
import json
import os

import jsonpath_rw_ext

from Aiplatform.app.com.rs.bean import ModelBean


class ConfigReader(object):
    '''
    This is a singleton class
    '''
    config_file_root = "D://Projects//AiAnalyticPlatform//Aiplatform//config//"
    system_config_property_file = ["system_config.properties"]
    tenant_config_json_file = "tenant_config.json"
    __instance  = None

    def __init__(self):
        self.__set_algo_config_object = set()
        if ConfigReader.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ConfigReader.__instance = self
            self.__sys_config_info = read_config(self.system_config_property_file)

            with open(ConfigReader.config_file_root + ConfigReader.tenant_config_json_file) as f:
                self.__tenant_config_info = json.load(f)
            self.load_algo_info_details()

    def get_tenant_config_info(self):
        return self.__tenant_config_info

    def get_algo_config_info_details(self):
        return list(self.__set_algo_config_object)

    def get_system_config_info(self):
        return self.__sys_config_info

    @staticmethod
    def getInstance() :
        """ Static access method. """
        if ConfigReader.__instance is None:
            ConfigReader()
        return ConfigReader.__instance

    def re_activate_config(self):
        self.__sys_config_info = read_config(self.system_config_property_file)
        self.__set_algo_config_object = set()
        with open(ConfigReader.config_file_root + ConfigReader.tenant_config_json_file) as f:
            self.__tenant_config_info = json.load(f)
        self.load_algo_info_details()

    def load_algo_info_details(self):
        tenant = [match.value for match in (jsonpath_rw_ext.parse('tenants[*].id').find(self.__tenant_config_info))]
        for l in tenant:
            model = [match.value for match in
                     (jsonpath_rw_ext.parse('tenants[?(id=' + l + ')].model[*].name').find(self.__tenant_config_info))]
            for m in model:
                versions = [match.value for match in (
                    jsonpath_rw_ext.parse('tenants[?(id=' + l + ')].model[?(name="' + m + '")].versions[*].id').find(
                        self.__tenant_config_info))]
                for v in set(versions):
                    version_info = [match.value for match in (jsonpath_rw_ext.parse(
                        'tenants[?(id=' + l + ')].model[?(name="' + m + '")].versions[?(id="' + v + '")]').find(self.__tenant_config_info))]
                    for v_info in version_info:
                        if dict(v_info).get("status") == "ACTIVE":
                            mb = ModelBean(l, m, v, v_info)
                            self.__set_algo_config_object.add(mb)

        print("Total Active Algo picked --> " ,self.__set_algo_config_object.__len__())
        for m in self.__set_algo_config_object:
            print(m.to_string())


def read_config(cfg_files):
    if cfg_files is not None:
        config = configparser.RawConfigParser()

        # merges all files into a single config
        for i, cfg_file in enumerate(cfg_files):
            cfg_file = ConfigReader.config_file_root + cfg_file
            if os.path.exists(cfg_file):
                config.read(cfg_file)
            else:
                print("file not found --> {}".format(cfg_file))

    return config