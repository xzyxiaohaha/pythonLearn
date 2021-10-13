# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 17:17
# @Author : zyxiao
# @File : 8字符串格式化.py
# @Software : {PyCharm}

price = 52
txt = "The price is {} dollars"
print(txt.format(price))
txt = "The price is {:.2f} dollars"
print(txt.format(price))
age = 20
name = "肖哈哈"
txt = "name is :{0},{0}'s age is {1}"
print(txt.format(name, age))
txt = "I have a {fruit}, it is very {adj}"
print(txt.format(fruit = "banana",adj = "delicious"))
