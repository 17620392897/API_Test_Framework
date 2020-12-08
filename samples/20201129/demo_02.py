import re

str2 = '{"tag":{"id":144,"name":"shanghai"}}'
v = re.findall('"id":(.+?),',str2)[0]
print(v)

