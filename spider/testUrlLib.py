# -*- codeing = utf-8 -*-
# @Time : 2021/8/4 21:58
# @Author : zyxiao
# @File : testUrlLib.py
# @Software : {PyCharm}

import urllib.request

#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))

#获取一个post请求(模拟用户登录)
import urllib.parse
# data=bytes(urllib.parse.urlencode({"name":"hello"}),encoding="utf-8")     #bytes()把数据转化成二进制数据包
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#测试get请求,超时处理
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as result:
#     print("timeout")
#     print(result)

response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.5)
print(response.status)   #返回状态200表示成功

try:
    print(response.status)   #返回状态418表示发现你是个爬虫
    response=urllib.request.urlopen("http://douban.com",timeout=0.5)
except urllib.error.HTTPError as result:
    print("发现你是个爬虫了哦")
    print(result)

response=urllib.request.urlopen("http://baidu.com",timeout=0.5)
print(response.getheaders())
for i in response.getheaders():
    print(i)
print("Sever是：",response.getheader("Server"))




url="http://httpbin.org/post"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
data=bytes(urllib.parse.urlencode({"name":"hello"}),encoding="utf-8")
req=urllib.request.Request(url=url,data=data,headers=headers,method="post")
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))



# url="http://www.douban.com"
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }
# data=bytes(urllib.parse.urlencode({"name":"hello"}),encoding="utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers)
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
