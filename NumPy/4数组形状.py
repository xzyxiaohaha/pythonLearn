# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 11:29
# @Author : zyxiao
# @File : 4数组形状.py
# @Software : {PyCharm
#
#
# }

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7,8]])
print(arr)
print(arr.shape)


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

