import requests
import json as complexjson
from common.logger import logger


class RequestMethod(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.session()

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None,
                    **kwargs):
        logger.info(f"接口请求地址 ==>> {url}")
        logger.info(f"接口请求方式 ==>> {method}")
        logger.info(f"接口请求头 ==>> {complexjson.dumps(headers, indent=4, ensure_ascii=False)}")
        logger.info(f"接口请求 params参数 ==>> {complexjson.dumps(params, indent=4, ensure_ascii=False)}")
        logger.info(f"接口请求体 data参数 ==>> {complexjson.dumps(data, indent=4, ensure_ascii=False)}")
        logger.info(f"接口请求体 json参数 ==>> {complexjson.dumps(json, indent=4, ensure_ascii=False)}")
        logger.info(f"接口上传附件 files参数 ==>> {files}")
        logger.info(f"接口 cookies参数 ==>> {complexjson.dumps(cookies, indent=4, ensure_ascii=False)}")

    def get(self, api_url, **kwargs):
        return self.request(api_url, "GET", **kwargs)

    def post(self, api_url, data=None, json=None, **kwargs):
        return self.request(api_url, "POST", data, json, **kwargs)

    def put(self, api_url, data=None, **kwargs):
        return self.request(api_url, "PUT", data, **kwargs)

    def delete(self, api_url, **kwargs):
        return self.request(api_url, "DELETE", **kwargs)

    def request(self, api_url, method, data=None, json=None, **kwargs):
        url = self.url + api_url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        elif method == "POST":
            return self.session.post(url, data, json, **kwargs)
        elif method == "PUT":
            if json:
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        elif method == "DELETE":
            return self.session.delete(url, **kwargs)
