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
    # savePath="豆瓣电影Top250.xls"   #\\进行转义，也可以直接在前面加“r”
    # saveData(dataList,savePath)
    dbPath="movie.db"
    saveData2DB(dataList,dbPath)
    # askURL("https://movie.douban.com/top250?start=0")

#影片详情链接的规则
findLink=re.compile(r'<a href="(.*?)">')   #创建正则表达式对象，表示规则
#影片图片的链接
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)  #re.S让换行符包含在字符中
#片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
#评分
findScore=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findEvaluate=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findIntroduce=re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findContent=re.compile(r'<p class="">(.*?)</p>',re.S)  #re.S忽视换行符



#获取网页
def getData(baseUrl):
    dataList=[]
    for i in range(0,10):   #调用获取页面信息的函数10次
        url=baseUrl+str(i*25)
        html=askURL(url)  #保存获取到的网页源码
        # print(html)
        # 2.逐一解析数据
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):   #查找符合要求的字符串，形成列表
            # print(item)  #测试查看电影item全部信息
            data=[]   #保存一部电影所有信息
            item=str(item)   #把item变成字符串

            #影片详情的链接
            link=re.findall(findLink,item)[0]   #re库通过正则表达式查找符合的内容(第一个)
            # print(link)
            data.append(link)     #添加链接

            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)    #添加图片

            titles = re.findall(findTitle, item)
            if len(titles)==2:
                chineseTitle=titles[0]
                data.append(chineseTitle)   #添加中国名
                foreignTitle=titles[1].replace("/","")   #外国名字前有"/"，需要替换成空格
                data.append(foreignTitle)   #添加外国名
            else:
                data.append(titles[0])
                data.append(' ')    #如果只有一个中文名，把外文名留空

            score = re.findall(findScore, item)[0]
            data.append(score)  # 添加评分

            evaluateNumber=re.findall(findEvaluate,item)[0]
            data.append(evaluateNumber)   #添加评价人数

            introduce=re.findall(findIntroduce,item)# 添加概述，此处的概述可能为空
            if len(introduce)!=0:
                data.append(introduce[0].replace("。",""))  #去掉句号
            else:
                data.append(" ")

            content=re.findall(findContent,item)[0]
            content=re.sub('<br(\s+)?/>(\s+)?',"",content)   #去掉<br/>,(\s+)?表示去掉里面一个或者多个字符
            content=re.sub("/","",content)  #替换“/”
            data.append(content.strip())  #strip()去掉前后的空格

            dataList.append(data)   #把处理好的一部电影放到datalist中
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
        f = open("test.txt", "a+",  encoding="utf-8")
        f.write(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    finally:
        f.close()  # 关闭文件
    return html

#保存数据到表格中
def saveData(dataList,savePath):
    book = xlwt.Workbook(encoding="utg-8",style_compression=0)  # 创建Workbook对象
    sheet = book.add_sheet("豆瓣电影top250",cell_overwrite_ok=True)  # 创建工作表,cell_overwrite_ok表示是否可以覆盖
    col=("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价人数","概况","相关内容")
    for i in range(0, 8):
        sheet.write(0,i,col[i])   #列名

    for i in range(0,250):
        print("第%d条"%i)
        data=dataList[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #数据

    book.save(savePath)

#创建初始化数据库
def init_db(dbPath):
    sql='''
        create table movie250(
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        fname varchar,
        score numeric,
        evaluateNumber numeric,
        introduce text,
        content text
        )
    '''
    conn=sqlite3.connect(dbPath)
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

#保存数据到数据库中
def saveData2DB(dataList,dbPath):
    init_db(dbPath)
    conn=sqlite3.connect(dbPath)
    cur=conn.cursor()

    for data in dataList:
        for index in range(len(data)):
            if index==4 or index==5:    #第5个和第六个只需要插入数值类型
                continue
            else:
                data[index] = '"' + data[index] + '"'


        sql='''
            insert into movie250(
            info_link, pic_link, cname, fname, score, evaluateNumber, introduce, content) 
            values (%s)'''%",".join(data)    #","join(data),把data里的数据用，连接
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print("...")



if __name__=="__main__":
    main()
    # init_db("movieTest.db")
    print("爬取完毕咯")