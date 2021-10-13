# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 17:03
# @Author : zyxiao
# @File : 6tryException.py
# @Software : {PyCharm}
try:
    print(x)
except:
    print("something was wrong!")

try:
    print("hello")
except:
    print("something was wrong !")
else:
    print("nothing was wrong,hahah")
finally:
    print("this senetense must be excute!")

x = 18
if x < 0:
    raise Exception("sorry, your number may be too low")

x = "hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")