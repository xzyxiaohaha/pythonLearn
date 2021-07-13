# -*- codeing = utf-8 -*-
# @Time: 2021/7/12 14:18
# @Author: zyxiao
# @File: 5元组.py
# @Software: PyCharm

#tuple不可修改，元素写在小括号里。元组的元素不可改变，但是元组里的list可以改变
#元组里如果只有一个元素，也必须加逗号
tup1=()
print(type(tup1))
tup2=(50)
print(type(tup2))
tup2=(50,)
print(type(tup2))
tup2=(50,60)
print(type(tup2))
tup=("111","aaa",23,"qwer")

#查
print(tup[0])
print(tup[1])
print(tup[-1])
print(tup[1:3])  #左闭右开


#增  (连接)
tup1=(1,2,3)
tup2=("a","b","c")
tup=tup1+tup2
print(tup)


#删
tup1=(1,2,3)
print(tup1)
del tup1 #删除整个元组，不可删除单一变量
print(tup1)



#改(不允许修改)

'''
tup=(12,34,23)
print(tup)
tup[0]=23
'''

