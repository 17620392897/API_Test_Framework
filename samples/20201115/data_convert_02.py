
a_dict = {'小红':[{'book1':'朝花夕拾'},{'book2':'红楼梦'}],
          '小绿':[{'book1':'呐喊'},{'book2':'红楼梦'}]}
data_list = []
for key,value in a_dict.items():
    b_dict = {}
    b_dict['name'] = key
    b_dict['books'] = value
    data_list.append(b_dict)
print(data_list)