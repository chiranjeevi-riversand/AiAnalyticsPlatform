# a simple function to read an array of configuration files into a config object
import os
import configparser


class ConfigReader(object):
    '''
    This is a singleton class
    '''
    file_root = "D://Projects//AiAnalyticPlatform//Aiplatform//config//"
    list_of_files = ["system_config.properties"]
    config = None
    __instance = None

    def __init__(self):
        if ConfigReader.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ConfigReader.__instance = self
            self.config = read_config(self.list_of_files)

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ConfigReader.__instance is None:
            ConfigReader()
        return ConfigReader.__instance


def read_config(cfg_files):
    if cfg_files is not None:
        config = configparser.RawConfigParser()

        # merges all files into a single config
        for i, cfg_file in enumerate(cfg_files):
            cfg_file = ConfigReader.file_root + cfg_file
            if os.path.exists(cfg_file):
                config.read(cfg_file)
            else:
                print("file not found --> {}".format(cfg_file))

    return config
