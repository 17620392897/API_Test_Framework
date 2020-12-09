import re


str1 = '{"access_token":"40_hNKwG7lmOfcnTipkgszM17fM6DN_ed0NGMKfNJzw4s_2PhJ8_4vCZpOWzifC61W09NmRylwylgEi9xPgDCyd3jZJbo3uHb0zq9AFpVP7iNgT41YfGG-G0vQOdlJG_r_9opZfl9tDAcV2tOuwZGYhAGASZR","expires_in":7200}'
str2 = '"access_token":"(.+?)"'

v = re.findall(str2,str1)

if v :
    print(True)
else:
    print(False)