import json


str1 = '{"access_token":"40_hNKwG7lmOfcnTipkgszM17fM6DN_ed0NGMKfNJzw4s_2PhJ8_4vCZpOWzifC61W09NmRylwylgEi9xPgDCyd3jZJbo3uHb0zq9AFpVP7iNgT41YfGG-G0vQOdlJG_r_9opZfl9tDAcV2tOuwZGYhAGASZR","expires_in":7200}'
# 实现一：检测key是否存在
json_obj = json.loads(str1)
if 'access_token' in json_obj.keys():
    print('True')
else:
    print('Flase')
# 实现二：检测多个key是否存在
print('--------------------------------')
check_keys = ['access_token','expires_in']
yes_no = [None]
for check_key in check_keys:
    if check_key in json_obj.keys():
        yes_no.append(True)
    else:
        yes_no.append(False)
if False in yes_no:
    print('False')
else:
    print('True')
