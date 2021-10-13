# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 12:39
# @Author : zyxiao
# @File : 5数组重塑.py
# @Software : {PyCharm}
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

newarr = arr.reshape(2, 3, 2)
print(newarr)
print(newarr.base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.shape(-1)
print(newarr)