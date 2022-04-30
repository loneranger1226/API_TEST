import json
import yaml
from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    def __init__(self, default=None):
        ConfigParser.__init__(self, defaults=default)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData(object):
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info(f"加载{file_path}文件......")
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info(f"读取数据 ==>> {data}")
        return data

    def load_json(self, file_path):
        logger.info(f"加载{file_path}文件......")
        with open(file_path, mode='r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"读取数据 ==>> {data}")
        return data

    def load_ini(self, file_path):
        logger.info(f"加载{file_path}文件......")
        config = MyConfigParser()
        config.read(file_path, encoding='utf-8')
        data = dict(config._sections)
        logger.info(f"读取数据 ==>> {data}")
        return data


file_data = ReadFileData()
