# -*- codeing = utf-8 -*-
# @Time : 2021/8/11 20:06
# @Author : zyxiao
# @File : testRe.py
# @Software : {PyCharm}

#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
#创建模式对象
pat=re.compile("AA")   #此处的AA是正则表达式，用来验证其他的字符串
m=pat.search("AAasdaAA")   #search  字符串被校验的内容


#没有模式对象
m=re.search("asd","Aasd")  #前面的字符串是规则（模板），后面的字符串是被校验的#<re.Match object; span=(1, 4), match='asd'>，左闭右开
print(m)
print(re.findall("a","werqAdfsAadsdfa"))#前面的字符串是规则（模板），后面的字符串是被校验的

print(re.findall("[A-Z]","ASDdasdasewrAefdsdA"))  #打印出大写字母

print(re.findall("[A-Z]+","ASDdasdasewrAefdsdA"))  #打印出大写字母(分别打印出连续的大写字母)

#sub(可以用于替换换行)
print(re.sub("a","B","abcdcasd"))  #在第三个字符串中找到a，用A来替换

#建议在正则表达式中，被比较的字符串前面加上r,不用担心转义字符的问题
a=r"\aabb-\'"
print(a)







