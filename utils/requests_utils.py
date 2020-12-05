# -!- coding: utf-8 -!-
import requests
import json
from utils.config_utils import local_config

class RequestsUtils:
    def __init__(self):
        self.hosts = local_config.HOSTS
        self.sessin = requests.session()
    def __get(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        response = self.sessin.get(url = url,
                                   params = json.loads(requests_info['请求参数（get）']),
                                   headers = requests_info['请求头部信息'])
        response.encoding = response.apparent_encoding  # 根据网页的内容分析网页的编码方式，防止乱码
        result = {
            'code':0,
            'response_code':response.status_code,
            'response_reason':response.reason,
            'response_headers':response.headers,
            'responser_body':response.text
        }
        return  result

    def __post(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        response = self.sessin.post(url=url,
                                    headers=requests_info['请求头部信息'],
                                   params=json.loads(requests_info['请求参数（get）']),
                                    json = json.loads(requests_info['请求参数（post）'])
                                   )
        response.encoding = response.apparent_encoding
        result = {
            'code': 0,
            'response_code': response.status_code,
            'response_reason': response.reason,
            'response_headers': response.headers,
            'responser_body': response.text
        }
        return result

    def request(self,step_info):
        request_type = step_info['请求方式']
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            result = self.__post(step_info)
        else:
            result = {'code':1,'result':'请求方式不支持'}
        return result

    def request_by_step(self,test_steps):
        for test_step in test_steps:
            result = self.request(test_step)
            print(result)
            if result['code'] !=0:
                break
        return result

if __name__ == '__main__':
    # req_post_dict = {'测试用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数（get）': '{"access_token":"39_7UqLDvOpS98IxuyTnuRwwEbtsUPgqdDtN5w-VgX-Tr1LRL4T1kGpW-nEYuJqEEOsiUumAwyrTO2lw4FnK0WkC8t2uikKwoE-rQdClqYC9bQNRNUrdb0nCtQe9_MLKVCwo9qVukfVMsxR2eJaNDWiAAAWMF"} ', '请求参数（post）': '{   "tag":{        "id" : 101   } } '}
    # req_get_dict = {'测试用例编号': 'api_case_01', '测试用例名称': '获取access_token接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': ''}
    step_list = [{'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数（get）': '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}', '请求参数（post）': ''}, {'测试用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数（get）': '{"access_token":"39_MXKfVtJCg2IgNz8hVcporEWd99neBhcGDoa_YpEzWoPEoF_4bzEh_zzgU17Ww0n_tou0-uS6VLwvswcC5sQ2I4uzNELvs7CtBlPy5H53Dl963vI3pnTvU1GK2I8nzM_6i8zcqz6xwsysCmkzJKWiAFASTF"} ', '请求参数（post）': '{ "tag" : { "name" : "广东"} } '}]
    requestsUtils = RequestsUtils()
    requestsUtils.request_by_step(step_list)
    # print(v)
