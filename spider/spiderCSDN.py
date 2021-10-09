# -*- codeing = utf-8 -*-
# @Time : 2021/8/20 15:33
# @Author : zyxiao
# @File : spiderCSDN.py
# @Software : {PyCharm}

import urllib.request,urllib.error
from bs4 import BeautifulSoup
import re   #正则表达式，进行文字匹配
import time
import random
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#链接的规则
findLink=re.compile(r'<a.*href="(.*?)".*')   #创建正则表达式对象，表示规则
def main2():
    url="https://blog.csdn.net/qq_41318914/article/details/119824383"
    head = {  # 模拟浏览器头部文件，向服务器发送消息
        # "user-agent"告诉服务器我们是什么类型的机器（浏览器）（本质上告诉浏览器，我们可以接收什么水平的文件内容）
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    print(html)

def main():
    baseUrl="https://blog.csdn.net/qq_41318914"
    data = getData(baseUrl)
    head1 = {  # 模拟浏览器头部文件，向服务器发送消息
        # "user-agent"告诉服务器我们是什么类型的机器（浏览器）（本质上告诉浏览器，我们可以接收什么水平的文件内容）
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    head2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    head3 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
    }
    head4 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
    }

    headList=[head1,head2,head3,head4]
    num=len(data)
    i=1
    while True:
        number=random.randint(0, 14)
        headIndex=random.randint(0,3)
        request = urllib.request.Request(data[number],headers=headList[headIndex])
        response = urllib.request.urlopen(request)
        # html = response.read().decode("utf-8")
        # print(html)
        print("访问的第",i,"个链接为：",data[number],"number=",number,"headIndex=",headIndex)
        time.sleep(4)
        i+=1;


    # while True:
    #     for item in data:
    #         print(item)
    #         request = urllib.request.Request(item)
    #         response = urllib.request.urlopen(request)
    #         # time.sleep(1)
    #         # html = response.read().decode("utf-8")
    #         # print(html)




    # print("进入main()")

def getData(baseUrl):
    data = []
    #1.得到一个url的网页内容
    head = {  # 模拟浏览器头部文件，向服务器发送消息
        # "user-agent"告诉服务器我们是什么类型的机器（浏览器）（本质上告诉浏览器，我们可以接收什么水平的文件内容）
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    request = urllib.request.Request(baseUrl,headers=head)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    # print(html)
    #2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("article", class_="blog-list-box"):  # 查找符合要求的字符串，形成列表
        item = str(item)  # 把item变成字符串
        # print(item)
        # print("-------------------")
        link = re.findall(findLink, item)[0]  # re库通过正则表达式查找符合的内容(第一个)，如果不加[0]，返回的是[' ']
        data.append(link)  # 添加链接
    # print(data)
    return data
    # print(data)
    # print(len(data))

if __name__ == '__main__':
    main()