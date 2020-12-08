# -!- coding: utf-8 -!-
import requests
import jsonpath
import re

session = requests.session()

get_param_dict={
    "grant_type":"client_credential",
    "appid":"wx8969c59ed2ed87de",
    "secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"
}

response = session.get(url='https://api.weixin.qq.com/cgi-bin/token',
                        params=get_param_dict)
response.encoding = response.apparent_encoding
body = response.text
value = re.findall('"access_token":"(.+?)"',body)[0]
print(value)

