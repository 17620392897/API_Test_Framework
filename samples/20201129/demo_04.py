import requests
import json
import re

json_obj = {"access_token":"40_hNKwG7lmOfcnTipkgszM17fM6DN_ed0NGMKfNJzw4s_2PhJ8_4vCZpOWzifC61W09NmRylwylgEi9xPgDCyd3jZJbo3uHb0zq9AFpVP7iNgT41YfGG-G0vQOdlJG_r_9opZfl9tDAcV2tOuwZGYhAGASZR","expires_in":7200}
except_str = '{"expires_in":7200}'
except_dict = json.loads(except_str)
print(except_dict.items())
print(json_obj.items())
# 方式一：
if list(except_dict.items())[0] in list(json_obj.items()):
    print(True)
else:
    print(False)

# 方式二：多项比对考虑
yes_no = []
for except_item in except_dict.items():
    if except_item in json_obj.items():
        yes_no.append(True)
    else:
        yes_no.append(False)
if False in yes_no:
    print(False)
else:
    print(True)
