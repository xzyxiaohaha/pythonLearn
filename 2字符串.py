# -*- codeing = utf-8 -*-
# @Time: 2021/7/7 16:21
# @Author: zyxiao
# @File: 2字符串.py
# @Software: PyCharm
word='字符串'
sentensce="这是一个句子"
paragraph='''
    这是一首
    优美的
     诗句啊
'''
print(word)
print(sentensce)
print(paragraph)

str="I'm a student!"
str2='I\'m a student!'
str3="hahah\\t"
print(str,"----",str2,"----",str3)

str="xiaozhenyu"
print(str[0:4])  #到达不了4  【起始位置：结束位置：步进值】
print(str[:4])
print(str[4:])

print("hello\nxia0")
print(r"hello\nxia0")  #在字符串加r表示显示原始字符串



#冒泡排序
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[12,43,54,34,98,45,3,23,4,96]
print("排序前的数组为：")
for i in range(len(arr)):
    print(arr[i],end="\t")
bubbleSort(arr)
print("排序后的数组为：")
for i in range(len(arr)):
    print(arr[i],end="\t")