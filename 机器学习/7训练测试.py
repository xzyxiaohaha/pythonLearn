# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 22:04
# @Author : zyxiao
# @File : 7训练测试.py
# @Software : {PyCharm}

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100)
# plt.scatter(x, y)
# plt.show()
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
# plt.scatter(train_x,train_y)
# plt.scatter(test_x,test_y)
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

from sklearn.metrics import r2_score
r2 = r2_score(train_y, mymodel(train_x))
print("训练集的多项式回归拟合度：", r2)
r2 = r2_score(test_y, mymodel(test_x))
print("测试集的多项式回归拟合度：", r2)
myline = np.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))

plt.show()

#预测新值
print(mymodel(5))



