20201117:
1、项目初始化配置 == 放到GitHub上
2、数据源处理：
2.1、config读取的封装
2.2、excel存放测试数据转换到代码中的处理
合并单元格数据处理 ==》 封装excel_utils ==》 把excel数据转换成测试用例业务数据（setdefault() 为了把用例步骤整合到
对应的测试编号中） ==》 封装testcase_data_utils ==》 形态变化：{[],[]}=={"":[],"":[]}==[{"case_id":'','case_step':[]},...]

20201205：
1、根据上一次Excel封装的测试数据，来进行requests封装
2、ast.literal_eval：转换为字典；  response.apparent_encoding：根据网页的内容分析网页的编码方式，防止乱码
3、requests_utils模块
request_by_step --》request --》 __get/__post
4、Excel为后续课程准备 增加了字段：取值方式、取值代码、取值变量

20201205:
1、利用jsonpath取出上个接口的返回值存放到临时的字典中
2、利用re和replace完成下一个接口使用上一个接口的返回值作为参数值