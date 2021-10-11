# -*- codeing = utf-8 -*-
# @Time : 2021/10/11 14:44
# @Author : zyxiao
# @File : 5RegEx.py
# @Software : {PyCharm}
import re
txt = "China is a great country"
x = re.search("^China.*country$",txt)
if (x):
    print("we have match it!")
else:
    print("not match chars")

txt = "i am xiaohaha"
x = re.findall("[a-m]",txt)
print(x)