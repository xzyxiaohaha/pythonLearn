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
txt = "that were be 25 dollars"
x = re.findall("\d",txt)
print(x)
txt = "hello world"
x = re.findall("he..o",txt)
print(x)
txt = "i amd fine, thaaaaanks for your invertation!"
x = re.findall("tha+",txt)
print(x)
x = re.findall("tha{3}",txt)
print(x)
x = re.findall("th|in",txt)
print(x)
x = re.findall("a",txt)
print(x)
x = re.search("fine",txt)
print("the first match char is start from:", x.start())
x = re.split("\s",txt)
print(x)
x = re.sub("\s","9",txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)
x = re.search("a", txt)
print(x)
str = "China is a great country"
x = re.search(r"\bC\w+", str)
print(x.span())
x = re.search(r"\bC\w+", str)
print(x.string)
x = re.search(r"\bC\w+", str)
print(x.group())


