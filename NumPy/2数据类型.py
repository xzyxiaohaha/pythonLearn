# -*- codeing = utf-8 -*-
# @Time : 2021/10/12 16:36
# @Author : zyxiao
# @File : 2数据类型.py
# @Software : {PyCharm}
import numpy as np
arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype="S")
print(arr)
print(arr.dtype)

import numpy as np
arr = np.array([1, 2, 3, 4], dtype="i4")
print(arr)
print(arr.dtype)

#无法将非整数字符串（比如 'a'）转换为整数（将引发错误）：
try:
    arr = np.array(["a", "2", "3"], dtype="i")
    print(arr)
except:
    print("无法将非整数字符串（比如 'a'）转换为整数（将引发错误）")

arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype("i")
newarr = arr.astype("int")
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3]) #0表示false,其他都为true
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


