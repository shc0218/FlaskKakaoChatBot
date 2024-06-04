import json
from os import path
import os

class ConfigTool:
    def __init__(self):
        self.__standard_format = {
            "neis_api_key": "",
            "neis_api_city_code": "",
            "neis_api_school_code": "",
        }
        self.__path = os.path.abspath('.') + "/config.json"
    def setup_config(self):
        if not path.exists(self.__path):
            f = open(self.__path, "w")
            f.write(json.dumps(self.__standard_format, indent="\t"))
            f.close()
    def get_config(self, key: str):
        with open(self.__path, 'r') as f:
            json_data = json.load(f)
        if key in json_data.keys():
            return json_data[key]
        else:
            return None