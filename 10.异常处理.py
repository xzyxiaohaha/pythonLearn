# -*- codeing = utf-8 -*-
# @Time : 2021/8/3 21:37
# @Author : zyxiao
# @File : 10.异常处理.py
# @Software : {PyCharm}
#捕获异常
try:
    print("-----test-----1---")

    f=open("123.txt","r")  #用只读模式打开一个不存在的文件会报错

    print("-----test-----2---")
except IOError:
    print("文件每找到哦，亲")
    pass

try:
    print(num)
except NameError:   #异常类型想要被捕获需要一致
    print("产生错误了")

#将多个错误同时捕获
try:
    print("-----test-----1---")
    f=open("123.txt","r")
    print("-----test-----2---")
    print(num)
except (NameError,IOError) :
    print("产生错误了")



#使用as result获取错误描述
try:
    print("-----test-----1---")
    f=open("123.txt","r")
    print("-----test-----2---")
    print(num)
except (NameError,IOError) as result:
    print("产生错误了")
    print(result)


#使用Exception捕获所以的异常
try:
    print("-----test-----1---")
    f=open("123.txt","r")
    print("-----test-----2---")
    print(num)
except Exception as result:
    print("产生错误了")
    print(result)

#try....finally和嵌套
'''
try:
    f=open("123.txt","r")
except Exception as result:
    print(result)
    print("发生异常")
finally:
    f.close()
    print("这里是一定会执行的finally")
'''


#嵌套
import time
try:
    f=open("test2.txt","r")
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("读完啦，关闭文件！")
except Exception as result:
    print(result)
    print("发生异常")

