# -*- codeing = utf-8 -*-
# @Time: 2021/7/12 16:46
# @Author: zyxiao
# @File: 8函数.py
# @Software: PyCharm

#函数定义
def printInfo():
    print("---------------")
    print("人生苦短，他要用python")

#函数调用
printInfo()

#带参数的函数
def add2Num(a,b):
    c=a+b
    print(c)

#带返回值的函数
def add2Num(a,b):
    return a+b

print(add2Num(12,13))

#返回多个值的函数
#python中不存在函数重载，因为python中参数传递的值可以为任意类型
def divid(a,b):
    shang=a/b
    yushu=a%b
    return shang,yushu   #可以返回多个结果

s,y=divid(5,2)  #需要使用多个值来保存返回内容
print(s,y)


#全局变量&局部变量
a=100
def test1():
    global a   #声明全局变量在函数中的标识符
    a=300
    print(a)

test1()
print(a)