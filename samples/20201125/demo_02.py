# -!- coding: utf-8 -!-
import re

str1 = '{"access_token":${token}}'
variables_list = re.findall('\\${\w+}',str1)
print(variables_list)

dict1 = {'token': 'ASDCCFE'}
# str1 = str1.replace(variables_list[0],'"%s"'%'ASDCCFE')
print(variables_list[0][2:-1])
str1 = str1.replace(variables_list[0],'"%s"'%dict1[variables_list[0][2:-1]])
print(str1)
#  需要达到的效果:{"access_token":"ASDCCFE"}  考虑：多个变量怎么办？ 不需要替换的情况怎么办？
str2 = '{"name":${n},"age":${a}}'
dict2 = {'n': 'xiaoming','a':10}
variables_list = re.findall('\\${\w+}',str2)
print(variables_list)
for v in variables_list:
    str2 = str2.replace(v,'"%s"'%dict2[v[2:-1]])
print(str2)

