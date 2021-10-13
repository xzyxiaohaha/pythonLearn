# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 18:50
# @Author : zyxiao
# @File : 1文件文件读写.py
# @Software : {PyCharm}
import win32clipboard

f = open("test.txt")   #等同于f = open("demofile.txt", "rt")
# print(f.read())
# print(f.read(5))
print(f.readline())

f = open("test.txt", "r")
print(f.readline())
print(f.readline())

f = open("test.txt", "r")
for i in f:
    print(i)
f.close()

f = open("test.txt", "a")  #a表示追加
f.write("啦啦啦啦")
f.close()
f = open("test.txt", "r")
print(f.read())

f = open("test.txt", "w")
f.write("cool,w可以覆盖整个文件哦")
f.close()
f=open("test.txt", "r")
print(f.read())

'''
"x" - 创建 - 将创建一个文件，如果文件存在则返回错误
"a" - 追加 - 如果指定的文件不存在，将创建一个文件
"w" - 写入 - 如果指定的文件不存在，将创建一个文件
'''
try:
    f = open("myfile.txt", "x")
except:
    print("myfile.txt已经创建过咯！")

f=open("myfile2.txt","w")
f.close()
import os
if os.path.exists("myfile2.txt"):
    os.remove("myfile2.txt")
else:
    print("myfile2.txt文件不存在")

#删除整个文件夹
import os
os.rmdir("test")


