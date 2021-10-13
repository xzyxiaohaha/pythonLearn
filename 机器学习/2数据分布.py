# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 20:28
# @Author : zyxiao
# @File : 2数据分布.py
# @Software : {PyCharm}

import numpy as np
import numpy.random

x = np.random.uniform(0.0, 5.0, 250)
print("创建一个包含 250 个介于 0 到 5 之间的随机浮点数的数组：", x)

import matplotlib.pyplot as plt
# x = np.random.uniform(0.0, 5.0, 10000)
# plt.hist(x, 5)
# plt.show()

#正态数据分布
# x = numpy.random.normal(5.0, 1.0, 100000)  #指定平均值为 5.0，标准差为 1.0。
# plt.hist(x, 100)
# plt.show()

#散点图
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# plt.scatter(x, y)
# plt.show()

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()