# -*- codeing = utf-8 -*-
# @Time : 2021/8/4 11:57
# @Author : zyxiao
# @File : spider.py
# @Software : {PyCharm}

from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error   #制定URL，获取网页数据
import xlwt  #进行excel操作
import sqlite3  #进行SQLite数据库操作
def main():
    baseUrl="https://movie.douban.com/top250?start="
    #1.获取网页
    dataList=getData(baseUrl)
    #3.保存数据
    savePath=".\\豆瓣电影Top250.xls"   #\\进行转义，也可以直接在前面加“r”
    # saveData(savePath)
    askURL("https://movie.douban.com/top250?start=0")


#获取网页
def getData(baseUrl):
    dataList=[]
    for i in range(0,10):   #调用获取页面信息的函数10次
        url=baseUrl+str(i*25)
        html=askURL(url)  #保存获取到的网页源码
        print(i)
        # 2.逐一解析数据

    return dataList

#得到制定一个url的网页内容
def askURL(url):
    head={   #模拟浏览器头部文件，向服务器发送消息
        #"user-agent"告诉服务器我们是什么类型的机器（浏览器）（本质上告诉浏览器，我们可以接收什么水平的文件内容）
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(html)
        f = open("test.txt", "a+",encoding="utf-8")
        f.write(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    finally:
        f.close()  # 关闭文件
    return html





def saveData(baseUrl):
    print("save")


if __name__=="__main__":
    main()