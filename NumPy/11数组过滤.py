# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 14:20
# @Author : zyxiao
# @File : 11数组过滤.py
# @Software : {PyCharm}
import numpy as np

arr = np.array([61, 62, 63, 64, 65])
x = [True, False, True, False, True]
newarr = arr[x]
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([61, 62, 63, 64, 65])
filter_arr = arr >62
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(newarr)

