# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 14:31
# @Author : zyxiao
# @File : 12随机数.py
# @Software : {PyCharm}

from numpy import random
#生成一个 0 到 100 之间的随机整数
x = random.randint(100)
print(x)

# 0 到 1 之间的随机浮点数。
x = random.rand()
print(x)

x = random.randint(100, size=(5))
print(x)

#生成有 3 行的 2-D 数组，每行包含 5 个从 0 到 100 之间的随机整数：
x = random.randint(100, size=(3, 5))
print(x)

x = random.rand(5)
print(x)

x = random.rand(3, 5)
print(x)

x = random.choice([3, 5, 7, 9])
print(x)
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
