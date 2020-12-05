# -!- coding: utf-8 -!-
import requests

session = requests.session()

response = session.get(url='http://www.hnxmxit.com/')
response.encoding = response.apparent_encoding  #  根据网页的内容分析网页的编码方式，防止乱码
print(response.text)

