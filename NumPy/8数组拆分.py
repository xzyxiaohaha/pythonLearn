# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 13:20
# @Author : zyxiao
# @File : 8数组拆分.py
# @Software : {PyCharm}
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.array_split(arr, 4)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

newarr = np.array_split(arr, 3, axis=1)  #沿行 (axis=1) 分割。
print(newarr)

newarr = np.hsplit(arr, 3)
print(newarr)

