# a simple function to read an array of configuration files into a config object
import configparser
import json
import os


class ConfigReader(object):
    '''
    This is a singleton class
    '''
    config_file_root = "D://Projects//AiAnalyticPlatform//Aiplatform//config//"
    system_config_property_file = ["system_config.properties"]
    tenant_config_json_file = "tenant_config.json"

    __instance  = None

    def __init__(self):
        if ConfigReader.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ConfigReader.__instance = self
            self.__sys_config_info = read_config(self.system_config_property_file)

            with open(ConfigReader.config_file_root + ConfigReader.tenant_config_json_file) as f:
                self.__tenant_config_info = json.load(f)

    def get_tenant_config_info(self):
        return self.__tenant_config_info

    def get_system_config_info(self):
        return self.__sys_config_info

    @staticmethod
    def getInstance() :
        """ Static access method. """
        if ConfigReader.__instance is None:
            ConfigReader()
        return ConfigReader.__instance


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