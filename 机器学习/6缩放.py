# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 21:51
# @Author : zyxiao
# @File : 6缩放.py
# @Software : {PyCharm}

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pandas.read_csv("cars.csv")
X = df["Weight", "Volume"]
y = df["CO2"]
scaledX = scale.fit_transform(X)
print("缩放后的值为：", scaledX)
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)
scaled = scale.transform([[2300, 1.3]])
predicetedCO2 = regr.predict([scaled[0]])
print(predicetedCO2)



