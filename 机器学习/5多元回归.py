# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 21:40
# @Author : zyxiao
# @File : 5多元回归.py
# @Software : {PyCharm}

import pandas
df = pandas.read_csv("cars.csv")
X = df[["Weight", "Volume"]]
y = df["CO2"]
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
print("系数是描述与位置变量的关系的因子：", regr.coef_)
