# -*- codeing = utf-8 -*-
# @Time : 2021/8/3 21:17
# @Author : zyxiao
# @File : 9.文件操作.py
# @Software : {PyCharm}
#w模式，文件如果不存在就新建，如果存在，就将其覆盖
#默认为r模式
#rb,rw表示以字节的形式进行读和写
f=open("test.txt","w")
f.write("hello,asd\n"
        "asdas\n"
        "asdasdas")
f.close() #关闭文件

#read()读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
f=open("test.txt","r")
content=f.read(7)
print(content)
content=f.read(1)  #往后再读一个字符，空格算一个字符
print(content)
f.close()

#readlines()一次性读取全部文件为列表，每行一个字符串元素
#readline（）一次读取一行
f=open("test.txt","r")
content=f.readlines()
print(content)
i=1
for temp in content:
    print("第",i,"行：",temp)
    i+=1
f.close()

import os
#os模块中的rename()可以完成对文件的重命名操作
os.rename("test.txt","test2.txt")