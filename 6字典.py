# -*- codeing = utf-8 -*-
# @Time: 2021/7/12 14:46
# @Author: zyxiao
# @File: 6字典.py
# @Software: PyCharm
#key-valuse键值对形式， key必须是唯一的,用大括号包含起来。

info={"name":"肖振宇","age":22,"project":"阜阳中考"}
#字典的访问
print(info["age"])
#访问不存在的键值
#print(info["asd"]) #直接访问不存在的键会报错


#使用get(),如果不存在，默认会返回None
print(info.get("asd"))

#使用get(),找不到，返回指定值
print(info.get("gender","男"))

#增
info["id"]=1234
print(info)
#删
del info["id"]
print(info)
#del info   #删除字典后再访问会报错

#info.clear();  #清空字典
print(info)

#改
info["name"]="xiaohaha"
print(info)

#查
print(info.keys())  #得到所有的键，列表方式
print(info.values()) #得到所有的值
print(info.items())  #得到所有的项


for key in info.keys():  #遍历所有的键
    print(key)

for value in info.values(): #遍历所有的值
    print(value)

for key,value in info.items():
    print(key,":",value)

myList=["a","b","c","d","e"]
print(enumerate(myList))
for i,x in enumerate(myList):
    print(i,":",x)