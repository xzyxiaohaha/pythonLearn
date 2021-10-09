# -*- codeing = utf-8 -*-
# @Time : 2021/8/6 21:37
# @Author : zyxiao
# @File : test.py
# @Software : {PyCharm}


import xlrd
import xlwt
if __name__ == '__main__':
    #excel文件处理
    '''
    book = xlrd.open_workbook('nameList.xlsx')  # 源excel文件
    sheet = book.sheet_by_index(1) #表示第几个sheet
    workbook = xlwt.Workbook(encoding='utf-8')  # 输出的excel文件编码格式

    worksheet = workbook.add_sheet('2019')  # 输出的sheet名字
    index = 0
    print(sheet.ncols)
    for i in range(0, sheet.ncols): #sheet.ncols表示一个sheet中的列数，2019年的sheet中一共有2107列
        cell=sheet.cell(0,i)  #获取第0行，第1 2 3 4 ......2107列单元格
        if i % 7 == 0 and i != 0:   #因为每7列一个重复，基于此设置i%7==0的判断条件，也就是每遍历7个单元格，就把index+1
            index += 1
        worksheet.write(index, i % 7, label=cell.value)  #将数据放到对应的单元格中
    workbook.save('newNameList.xls')  # 保存，并设置输出的文件名
'''
    x,y,z="Orange","Banana","Cherry"
    x=y=z="banana"
    print(x)
    print(y)
    print(z)
    a = 2+3j
    print(a)
    print(type(a))
import random
print(random.randrange(1,10))
a=" Hello , world "
print(a.strip())
print(a.lower())
print(a.upper())
a=a.upper()
print(a.split(","))
txt="hello,i am xiaozhenyu"
print("xiaozhenyu" in txt)
print("xiaozhneyu" not in txt)
a="hello"
b="world"
print(a+b)
age=63
a="my age is :"
print(a,age)
x=200
print(isinstance(x,str))
print(6%3)
list1=[54,12,5,56,84,2,45]
list1.sort()
print(list1)
print(list1.pop())
tuple1=("haha","lalala","banana")
print(tuple1)
print(len(tuple1))
tuple2=("asd",)
print(type(tuple2))
print(tuple1.index("lalala"))
thisset={"asd","wqe","234","ty"}
for x in thisset:
    print(x)
thisset2={"qwe",123,23,}
for x in thisset2:
    print(x)
thisset3=thisset.union(thisset2)
print(thisset3)
thisDictionary={
    "brand":"APPLE",
    "model":123,
    "year":2000
}
print(thisDictionary)
child1 = {
  "name" : "Phoebe Adele",
  "year" : 2002
}
child2 = {
  "name" : "Jennifer Katharine",
  "year" : 1996
}
child3 = {
  "name" : "Rory John",
  "year" : 1999
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Phoebe", "Jennifer", "Rory")

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Bill", 63)

print(p1.name)
print(p1.age)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bill", 63)
p1.myfunc()


import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
