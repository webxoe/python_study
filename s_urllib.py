# encoding: utf-8
from urllib import request
from urllib import parse

resp = request.urlopen("http://www.baidu.com")
# 打印所有数据
# print(resp.read())

# 打印指定的字符串个数
print(resp.read(20))


# 打印一行数据
# print(resp.readline())

# 打印状态码
print(resp.getcode())

# 下载文件
request.urlretrieve('http://pic.netbian.com/uploads/allimg/200216/220418-158186185883c8.jpg', 'bizhi.jpg')

# url编码
params = {'name': '张三', 'age': 20, 'greet': 'Hello world'}
result = parse.urlencode(params)
print(result)





