# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 21:12
# @Author : zyxiao
# @File : 3线性回归.py
# @Software : {PyCharm}

import matplotlib.pyplot as plt
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
    return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
#r 平方值的范围是 0 到 1，其中 0 表示不相关，而 1 表示 100％ 相关。
print(r)
#预测一辆有 10年车龄的汽车的速度：
speed = myfunc(10)
print("预测的速度为：", speed)
