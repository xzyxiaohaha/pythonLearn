# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 13:00
# @Author : zyxiao
# @File : 7NumPy数组连接.py
# @Software : {PyCharm}
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))  #沿行堆叠
print(arr)
arr = np.vstack((arr1, arr2))   #沿列堆叠
print(arr)
arr = np.dstack((arr1, arr2))     #dstack() 沿高度堆叠
print(arr)


