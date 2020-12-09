str1 = {"errcode":45157,"errmsg":"invalid tag name hint: [UGeFv0I2e-Lp1iza] rid: 5fd071b9-10688309-58e7643a"}
check_data = 'tag'

def key_check( check_data):
    key_list = check_data.split(',')
    tem_result = []
    for key in key_list:
        if key in str1.keys():
            tem_result.append(True)
        else:
            tem_result.append(False)
    if False in tem_result:
        return False
    else:
        return True

print(key_check(check_data))