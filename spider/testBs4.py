# -*- codeing = utf-8 -*-
# @Time : 2021/8/6 17:38
# @Author : zyxiao
# @File : testBs4.py
# @Software : {PyCharm}

'''
BeautifulSoup将复杂的HTML文档转化成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种

- Tag
- NavigableString
- BeautifulSoup
- Comment

'''
from bs4 import BeautifulSoup
file=open("./baidu.html","rb")
html=file.read()
bs=BeautifulSoup(html,"html.parser")

#1.bs4.element.Tag 标签及其内容，拿到他所找到的第一个内容
print(type(bs.title))
print(bs.title)
print(bs.a)

#2.bs4.element.NavigableString 标签里的内容（字符串）
print(bs.title.string)
print(type(bs.title.string))
print(bs.a.attrs)  #拿到一个标签里的属性

#3.bs4.BeautifulSoup 表示整个文档
print(type(bs))
print(bs.name)
print(bs)

#4.bs4.element.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号
print(bs.a.string)
print(type(bs.a.string))
print("---------------------------------------------")
#文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])
# for i in bs.head.contents:
#     print(i)

#文档的搜索
#1.字符串过滤，查找与字符串完全匹配的内容
# t_list=bs.find_all("a")

import re
#2.正则表达式搜索，使用search()方法来匹配内容,包含“a”的都显示出来
# t_list=bs.find_all(re.compile("a"))
# print(t_list)

#3.方法：传入一个函数（方法），根据函数的要求来搜索
#把标签里面有name的标签整个获取出来
# def name_is_exits(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exits)
# print(t_list)

#4.kwargs 参数
# t_list=bs.find_all(id="head")
# t_list=bs.find_all(id=True)
# t_list=bs.find_all(class_="mnav")
# t_list=bs.find_all(class_=True)
# t_list=bs.find_all(href="http://tieba.baidu.com")
# print(t_list)

#5.text参数
# t_list=bs.find_all(text="hao123")
# t_list=bs.find_all(text=["hao123","地图","贴吧"])
# t_list=bs.find_all(text=re.compile("\d"))   #将所有的“数字”文本展现出来，用正则表达式查找特定文本的内容（标签里的字符串）
# print(t_list)

#6.limit参数(限制能够获取多少个)
# t_list=bs.find_all("a",limit=3)
# print(t_list)


#7.选择器
# t_list=bs.select("title")  #通过标签来查找

# t_list=bs.select(".mnav")  #通过类名来查找

# t_list=bs.select("#u1")    #通过id来查找

# t_list=bs.select("a[name='tj_briicon']")  #通过属性来查找（<a>标签里，name属性为tj_briicon的标签）

t_list=bs.select("head>title")  #通过子标签来查找

t_list=bs.select(".mnav ~ .bri") #mnav层次的兄弟，且兄弟名为bri
print(t_list)
print(t_list[0].get_text())    #get_text()获取标签之间的文本
