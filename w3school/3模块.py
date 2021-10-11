# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 11:17
# @Author : zyxiao
# @File : 3模块.py
# @Software : {PyCharm}
from test1 import t1 as ha
print(ha.add(10,5))
print(ha.Person)
import platform
print(platform.system())
print(dir(platform))
print(platform.version())
import re
print(type(re))
from re import search
print(type(search))