# -*- codeing = utf-8 -*-
# @Time : 2021/8/4 21:58
# @Author : zyxiao
# @File : testUrlLib.py
# @Software : {PyCharm}

import urllib.request
response=urllib.request.urlopen("http://www.baidu.com")
print(response.read())