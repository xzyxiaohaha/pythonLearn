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
    baseUrl="https://movie.douban.com/top250?stat="
    #1.获取网页
    dataList=getData(baseUrl)
    #3.保存数据
    savePath=".\\豆瓣电影Top250.xls"   #\\进行转义，也可以直接在前面加“r”
    saveData(savePath)
#获取网页
def getData(baseUrl):
    dataList=[]
    #2.逐一解析数据
    return dataList

def saveData(baseUrl):
    print("save")


if __name__=="__main__":
    main()