# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 13:05
# @Author : zyxiao
# @File : 4日期.py
# @Software : {PyCharm}
import datetime
x=datetime.datetime.today()
print(x)
print(x.year)
print(x.strftime("%A"))
x=datetime.datetime(2022,5,31)
print(x)
print(x.strftime("%B"))
