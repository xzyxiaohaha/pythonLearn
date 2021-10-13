# -*- codeing = utf-8 -*-
# @Time : 2021/10/12 15:46
# @Author : zyxiao
# @File : 1数组索引裁切.py
# @Software : {PyCharm}
import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(np.__version__)
print(type(arr))

arr = np.array((1, 2, 3, 4, 5))
print(arr)

arr1 = np.array(61) #0-D
print(arr1)

arr2 = np.array([1, 2, 3]) #1-D
print(arr2)

arr3 = np.array([[1, 2, 3],[4, 5, 6]]) #2-D
print(arr3)

print("asd")
arr4 = np.array([[[1, 2, 3],[4, 5, 6]],[[1, 2, 3],[4, 5, 6]]]) #3-D
print(arr4)

print(arr1.ndim)   #查看数组的维度
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("number of dimensions :", arr.ndim)

arr = np.array([1, 2, 3, 4])
print(arr[0])

#访问第一维中的第二个元素
print("2nd element on 1st dim:", arr3[0, 1])

#访问第二维中的第三个元素
print("5th element on 2nd dim:", arr3[1, 2])

#访问第一个数组的第二个数组的第三个元素
print("一个数组的第二个数组的第三个元素:", arr4[0, 1, 2])

#打印第二个维中的的最后一个元素：
print("last element from 2nd dim:", arr3[1, -1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])  #实际下标是0，1，2，3，4，5，6
print(arr[1:5])
print(arr[5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])   #-1表示最后一位
# print(arr[-3:1]) 数组越界

print(arr[1:5:2]) #从索引 1 到索引 5，返回相隔的元素

print(arr[::2]) #返回数组中相隔的元素

#裁切2-D数组，从第二个元素开始，对从索引 1 到索引 4（不包括）的元素进行切片：
arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#从两个元素中返回索引 2：
print(arr[0:2, 2])

#从两个元素裁切索引 1 到索引 4（不包括），这将返回一个 2-D 数组：
print(arr[0:2, 1:4])


