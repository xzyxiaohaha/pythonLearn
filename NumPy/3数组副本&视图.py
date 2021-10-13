# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 11:03
# @Author : zyxiao
# @File : 3数组副本&视图.py
# @Software : {PyCharm}

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 61
print(arr)
print(x)

y = arr.view()
x[0] = 61
print(arr)
print(y)


#每个 NumPy 数组都有一个属性 base，如果该数组拥有数据，则这个 base 属性返回 None。否则，base 属性将引用原始对象。
#副本返回none,视图返回原始数组
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
