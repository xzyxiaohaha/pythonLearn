# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 15:08
# @Author : zyxiao
# @File : 13ufuncs.py
# @Software : {PyCharm}

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
    z.append(i + j)
print(z)

import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)

