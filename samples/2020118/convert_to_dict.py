# -!- coding: utf-8 -!-
import json
import ast

str1 = '{"grant_type":"client_credential","appid":"wx8969c59ed2ed87de","secret":"e3d1d2bc3db1f1f239582eaf7ffcdcfa"}'
jsondata = json.loads(str1)
print(type(jsondata))
dict1 = eval(str1)
print(dict1)
print(type(dict1))
dict2 = ast.literal_eval(str1)
print(dict2)
print(type(dict2))
