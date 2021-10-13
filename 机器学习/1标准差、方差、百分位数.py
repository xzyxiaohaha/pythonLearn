# -*- codeing = utf-8 -*-
# @Time : 2021/10/13 16:48
# @Author : zyxiao
# @File : 1标准差、方差、百分位数.py
# @Software : {PyCharm}
import numpy
import numpy as np
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.mean(speed)  #平均数
print("平均值为：", x)

x = numpy.median(speed)  #中值
print("中值为：", x)

from scipy import stats
x = stats.mode(speed)    #众数
print("众数为：", x)

speed = [86, 87, 88, 86, 87, 85, 86]
x = numpy.std(speed)
print("标准差：", x)

speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.var(speed)
print("方差是：", x)
x = numpy.std(speed)
print("标准差是：", x)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print("(75％ 的人是 43 岁或以下)百分位数：", x)
x = numpy.percentile(ages, 90)
print("百分位数", x)

