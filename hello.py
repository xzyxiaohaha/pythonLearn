# -*- codeing = utf-8 -*-
# @Time : 2021/7/6 16:28
# @Author : zyxiao
# @File : hello.py
# @Software : PyCharm

#这是单行注释
print("hello py") #注释
'''
第一行注释
第二行注释

'''
#格式化输出
age=18
print("你的年龄是：%d岁！"%age)
print("你的名字是：%s，国籍是：%s啊"%("小肖","中国"))

print("aaa","bbbb","ccccc")
print("www","baidu","com",sep=".")

print("hello",end="")
print("python",end="\t")
print("i am robot",end="\n")
print("----")

'''
password=input("请输入密码：")
print("您的1密码是:%s"%password)
print("您的2密码是:",password)
print("您的3密码是:"+password)
print(type(password))
password=int(password)
print(password+100)
#使用%s、%d时，变量类似必须匹配；使用“，”时，都可以；“+”号只能用于字符串的拼接，不能拼接int型
'''
#print(10<<2)
#python中非0和非空值为True,0或者None为False
a=10
b=20
print (a and b)


'''
a=int(input("请输入一个数字："))
if a<10:
    print("输入的值小于10")
elif a>=10 and a<100:
    print("a大于等于10，小于100")
elif a>=100:
#else:     elif和else可以一起使用
    print("a大于等于100")
'''


import random   #引入随机库
x=random.randint(0,2) #生成[0,2]的随机数
print("生成的随机数为：",x)