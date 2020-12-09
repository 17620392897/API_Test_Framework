# -!- coding: utf-8 -!-
import requests
import json
import jsonpath
import re
from utils.config_utils import local_config
from utils.check_utils import CheckUtils

class RequestsUtils:
    def __init__(self):
        self.hosts = local_config.HOSTS
        self.sessin = requests.session()
        self.tmp_variables = {}
    def __get(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        variable_list = re.findall('\\${\w+}',requests_info['请求参数（get）'])
        for variable in variable_list:
            requests_info['请求参数（get）'] = requests_info['请求参数（get）'].replace(
                variable,'"%s"'%self.tmp_variables[variable[2:-1]])
        response = self.sessin.get(url = url,
                                   params = json.loads(requests_info['请求参数（get）']),
                                   headers = requests_info['请求头部信息'])
        response.encoding = response.apparent_encoding  # 根据网页的内容分析网页的编码方式，防止乱码
        if requests_info['取值方式'] == 'jsonpath取值':
            value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
            self.tmp_variables[requests_info['取值变量']] = value
        elif requests_info['取值方式'] == '正则取值':
            value = re.findall(requests_info['取值代码'],response.text)[0]
            self.tmp_variables[requests_info['取值变量']] = value
        result = CheckUtils(response).run_check(requests_info['断言类型'],requests_info['期望结果'])
        return  result

    def __post(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        get_variable_list = re.findall('\\${\w+}', requests_info['请求参数（get）'])
        for variable in get_variable_list:
            requests_info['请求参数（get）'] = requests_info['请求参数（get）'].replace(
                variable,'"%s"'%self.tmp_variables[variable[2:-1]])
        post_variable_list = re.findall('\\${\w+}', requests_info['请求参数（post）'])
        for variable in post_variable_list:
            requests_info['请求参数（post）'] = requests_info['请求参数（post）'].replace(variable,
                                            '"%s"'%self.tmp_variables[variable[2:-1]])
        response = self.sessin.post(url=url,
                                    headers=requests_info['请求头部信息'],
                                    params=json.loads(requests_info['请求参数（get）']),
                                    json = json.loads(requests_info['请求参数（post）'])
                                   )
        response.encoding = response.apparent_encoding
        if requests_info['取值方式'] == 'jsonpath取值':
            value = jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
            self.tmp_variables[requests_info['取值变量']] = value
        elif requests_info['取值方式'] == '正则取值':
            value = re.findall(requests_info['取值代码'],response.text)[0]
            self.tmp_variables[requests_info['取值变量']] = value
        result = CheckUtils(response).run_check(requests_info['断言类型'],requests_info['期望结果'])
        return result

    def request(self,step_info):
        request_type = step_info['请求方式']
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            result = self.__post(step_info)
        else:
            result = {'code':2,'result':'请求方式不支持'}
        print(self.tmp_variables)
        return result

    def request_by_step(self,test_steps):
        for test_step in test_steps:
            result = self.request(test_step)
            # print(result)
            if result['code'] !=0:
                break
            print(result)
        return result

if __name__ == '__main__':
    # req_post_dict = {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数（get）': '{"access_token":"40_Kd2QNGXcDg1CN7YiI6zJCfG2ti1scJ2gmWmgUWri_p08EmJrY7SYlCiSpA_3OxqAeYG3O6a5isPCX5Ei8Q1UIUSHjs9M_8feDSptYVSmB6_ZWSGvPqIs6lV17oNK_WM9GRCUauZx99xQh_-2HUWfACANAC"} ', '请求参数（post）': '{   "tag":{        "id" : 101   } } '}
    # # req_get_dict = {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': ''}
    # step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': ''}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数（get）': '{"access_token":"40_Pfgl7rdeLrTqpNbPfbm7erriE22z7mDbJoiF6Su4Ki9x3wksqWfzdiYnE45l2G84VC-2dGDQQ8qTN5gBvsxUYLydQ3x-kWMdy6z0ljmfOsj7caw60sQp6rUhB_4p5CB9M6Xno3qV66vjLj2mJLSjAFAMOV"} ', '请求参数（post）': '{ "tag" : { "name" : "广东牛"} } '}]
    # requestsUtils = RequestsUtils()
    # requestsUtils.request_by_step(step_list)
    # print(v)
    # get_step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': '', '取值方式': 'jsonpath取值', '取值代码': '$.access_token', '取值变量': 'token'}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数（get）': '{"access_token":${token}}', '请求参数（post）': '{ "tag" : { "name" : "广东101"} } ', '取值方式': '无', '取值代码': '', '取值变量': ''}]
    # post_step_list = [{'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': '', '取值方式': 'jsonpath取值', '取值代码': '$.access_token', '取值变量': 'token'}, {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数（get）': '{"access_token":${token}}', '请求参数（post）': '{ "tag" : { "name" : "hunan666"} } ', '取值方式': 'jsonpath取值', '取值代码': '$.tag.id', '取值变量': 'tag_id'}, {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数（get）': '{"access_token":${token}}', '请求参数（post）': '{   "tag":{        "id" : ${tag_id}   } } ', '取值方式': '无', '取值代码': '', '取值变量': ''}]
    # requestsUtils = RequestsUtils()
    # r = requestsUtils.request_by_step(post_step_list)
    # print(r['responser_body'])
    # step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': '', '取值方式': '正则取值', '取值代码': '"access_token":"(.+?)"', '取值变量': 'token'}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数（get）': '{"access_token":${token}}', '请求参数（post）': '{ "tag" : { "name" : "广东444"} } ', '取值方式': '无', '取值代码': '', '取值变量': ''}]

    step_list = [{'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': '', '取值方式': '无', '取值代码': '', '取值变量': '', '断言类型': '正则比对', '期望结果': '"access_token":"(.+?)"'}]
    requestsUtils = RequestsUtils()
    r = requestsUtils.request_by_step(step_list)







