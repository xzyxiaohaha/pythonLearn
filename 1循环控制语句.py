# -*- codeing = utf-8 -*-
# @Time: 2021/7/7 10:55
# @Author: zyxiao
# @File: 1循环控制语句.py
# @Software: PyCharm
for i in range(5):   #0,1,2,3,4
    print(i,end="|")
print("-----------------")

for i in range(1,10,3):  #不包含10的！！！
    print(i,end="|")
print("-----------------")

for i in range(-10,100,30):
    print(i,end="|")
print("-----------------")

name="xiaozhenyu"
for i in name:
    print(i,end="\t")
print("-----------------")

arr=["aa","bb","cc","dd"]
for i in range(len(arr)):
    print(i,arr[i])
print("-----------------")

i=0;
while i < 9:
    print("当前是第", i + 1, "次执行循环")
    i += 1

arr=[34,12,65,34,78,45,43,9,67,99]
for i in range(len(arr)):
    print(arr[i],end="|")

#1-100求和
counter = 1
sum = 0
while counter <= 100:
    sum += counter
    counter += 1
print(sum)

counter=0
while counter<5:
    print("%d小于5"%counter)
    counter+=1
else:
    print(counter,"大于等于5")


print("我事谁"*30)

'''
b=2;
for i in range(1,10):
    for j in range(1,b):
        print(j,"*",i,"=",i*j,end="\t")
    b += 1;
    print("\r")
'''

'''
i=1
j=1
a=1
while i<=9:
    while j<=a:
        print(j,"*",i,"=",i*j,end="\t")
        j+=1
    j=1
    print("\r")
    i+=1;
    a+=1;
'''


