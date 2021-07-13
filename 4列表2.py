# -*- codeing = utf-8 -*-
# @Time: 2021/7/12 10:15
# @Author: zyxiao
# @File: 4列表2.py
# @Software: PyCharm
myList=["a","b","c","a","e"]
print(myList.index("a",0,4)) #index可以获取列表中某一段区间的下标位置，遵循左闭右开原则[1,4)
print(myList.count("s"))  #计算某个元素出现几次

print("原列表：",myList)
myList.reverse()
print("列表反转：",myList)
myList.sort()
print("升序排序",myList)  #升序排序
myList.sort(reverse=True)  #降序排序
print("降序排序：",myList)



schoolName=[["北京大学","清华大学",["浙江大学","南京大学"]],["安徽大学","河南大学","黑龙江大学"],["芜湖大学","六安大学"]]
print(schoolName)
print(schoolName[0][2][0])

import random
print(random.randint(0,2))  #随机数包括0，1，2
offices=[[],[],[]]
names=["a","b","c","d","e","f","g","h"]
for name in names:
    index=random.randint(0,2)
    offices[index].append(name)

print(offices)

i=1
for office in offices:
    print("第",i,"个办公室的人数为:",len(office))
    i+=1;
    print("办公室有这些人：",end="\t")
    for name in office:
        print(name,end=" | ")
    print()