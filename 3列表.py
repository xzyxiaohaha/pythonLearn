# -*- codeing = utf-8 -*-
# @Time: 2021/7/8 10:18
# @Author: zyxiao
# @File: 3列表.py
# @Software: PyCharm

list =["abcd",786,2.23,"todo",90]
print(list[1:3])
tinyList=["haha",123]
print(list+tinyList*3)
print(list[0:-1])  #索引值0为开始值，-1为末尾的开始位置
print(list[-1])   #-1为倒数第一个元素，-2为倒数第二个元素，，，，

for i in list:
    print(i,end="\t")

length=len(list)
i=0
while i<length:
    print(list[i],end="\t")
    i+=1


#增 append()

#nameTemp=input("在末尾追加一个元素：")
nameTemp="xiaozhenyu"
list.append(nameTemp)
print(list)

#增 extend()
a=[1,2]
b=[3,4]
a.append(b)
print(a)
a.extend(b)  #将b的元素，逐一加入到a中
print(a)

#插入 insert()
a=[0,1,2]
a.insert(1,3)  #0,3,1,2
print(a)

#删除 del在指定的位置删除一个元素   pop弹出末尾最后一个元素
#remove删除指定内容的元素,如果有重复数据，删除的是第一个重复数据
movieName=["速度与激情","黑客帝国","送你一朵小红花","速度与激情","悬崖之上","功夫"]
print(movieName)
del movieName[2]
print(movieName)
movieName.pop()
print(movieName)
movieName.remove("速度与激情")
print(movieName)


#改
movieName[1]="觉醒年代"
print(movieName)

#查
findName=input("请输入需要查找的电影名称:")
if findName in movieName:
    print("存在此电影")
else:
    print("不存在")

