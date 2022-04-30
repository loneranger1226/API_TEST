import os
from Request.request import RequestMethod
from common.read_data import file_data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "settings.ini")
api_url = file_data.load_ini(data_file_path)["host"]["api_url"]


class User(RequestMethod):
    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/api/sys/login", **kwargs)

    def employ_list(self, **kwargs):
        return self.get(f"/api/sys/user?", **kwargs)

    def employ_add(self, **kwargs):
        return self.post("/api/sys/user", **kwargs)

    def employ_update(self, user_id, **kwargs):
        return self.put(f"/api/sys/user/{user_id}", **kwargs)

    def employ_info(self, user_id, **kwargs):
        return self.get(f"/api/sys/user/{user_id}", **kwargs)

    def employ_delete(self, user_id, **kwargs):
        return self.delete(f"/api/sys/user/{user_id}", **kwargs)


user = User(api_url)
