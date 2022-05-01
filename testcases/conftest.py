import os
import pytest
import allure
from API.user import user
from common.read_data import file_data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = file_data.load_yaml(data_file_path)
    except Exception as e:
        pytest.skip(str(e))
    else:
        return yaml_data


api_data = get_data("api_test_data.yml")
print(api_data)