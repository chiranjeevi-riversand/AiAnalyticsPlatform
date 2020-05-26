
# a simple function to read an array of configuration files into a config object
import os
from configparser import ConfigParser


class Config_reader():

    list_of_files = ["app_config.properties"]
    config = None

    def __init__(self,properties_file: str):
        config = read_config(properties_file)

def read_config(self, cfg_files ):
    if cfg_files is not None:
        config_parser = ConfigParser.RawConfigParser()

        # merges all files into a single config
        for i, cfg_file in enumerate(cfg_files):
            if os.path.exists(os.path.join("./../../../", cfg_file)):
                config_parser.read(cfg_file)

        return config_parser