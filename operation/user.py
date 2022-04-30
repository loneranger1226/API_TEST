from Request.request_result import RequestResult
from API.users import user
from common.logger import logger


def login(mobile, password):
    result = RequestResult()
    json_data = {
        "mobile": mobile,
        "password": password
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.login(json=json_data, headers=header)
    res_json = res.json()
    result.msg = res_json.get("message")
    if res_json.get("code") == 10000:
        result.success = True
        result.token = "Bearer " + res_json.get("data")
    else:
        result.error = f"接口返回码是【{res_json.get('code')}】，返回信息：{result.msg}"
    logger.info(f"登录用户 ==>> 返回结果 ==>> {res.text}")


def employ_list(page, size, token):
    result = RequestResult()
    json_data = {
        "page": page,
        "size": size
    }
    header = {
        "Authorization": token
    }
    res = user.employ_list(params=json_data, headers=header)
    res_json = res.json()
    if res_json.get("code") == 10000:
        result.success = True
    else:
        result.error = f"接口返回码是【{res_json.get('code')}】，返回信息：{result.msg}"
    logger.info(f"查询员工列表 ==>> 返回结果 ==>> {res.text}")


def employ_add(username, mobile, work_number, token, timeOfEntry=None, formOfEmployment=None, departmentId=None,
               departmentName=None, correctionTime=None):
    result = RequestResult()
    json_data = {
        "username": username,
        "mobile": mobile,
        "workNumber": work_number,
        "timeOfEntry": timeOfEntry,
        "formOfEmployment": formOfEmployment,
        "departmentId": departmentId,
        "departmentName": departmentName,
        "correctionTime": correctionTime
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = user.employ_add(json=json_data, headers=header)
    res_json = res.json()
    result.msg = res_json.get("message")
    if res_json.get("code") == 10000:
        result.success = True
    else:
        result.error = f"接口返回码是【{res_json.get('code')}】，返回信息：{result.msg}"
    logger.info(f"添加员工 ==>> 返回结果 ==>> {res.text}")


def employ_update(user_id, token, username=None, password=None, department_id=None, department_name=None):
    result = RequestResult()
    json_data = {
        "username": username,
        "password": password,
        "department_id": department_id,
        "department_name": department_name,
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = user.employ_update(user_id, json=json_data, headers=header)
    res_json = res.json()
    result.msg = res_json.get("message")
    if res_json.get("code") == 10000:
        result.success = True
    else:
        result.error = f"接口返回码是【{res_json.get('code')}】，返回信息：{result.msg}"
    logger.info(f"修改员工 ==>> 返回结果 ==>> {res.text}")


def employ_info(user_id, token):
    result = RequestResult()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = user.employ_info(user_id, headers=header)
    res_json = res.json()
    result.msg = res_json.get("message")
    if res_json.get("code") == 10000:
        result.success = True
    else:
        result.error = f"接口返回码是【{res_json.get('code')}】，返回信息：{result.msg}"
    logger.info(f"查询员工 ==>> 返回结果 ==>> {res.text}")


def employ_delete(user_id, token):
    result = RequestResult()
    header = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    res = user.employ_delete(user_id, headers=header)
    res_json = res.json()
    result.msg = res_json.get("message")
    if res_json.get("code") == 10000:
        result.success = True
    else:
        result.error = f"接口返回码是【{res_json.get('code')}】，返回信息：{result.msg}"
    logger.info(f"删除员工 ==>> 返回结果 ==>> {res.text}")

# login("13800000002", "123456")
# employ_add("武xxaa琦", "13739880001", "123")
# employ_update("小猪xx01")
# employ_info()
