# -*- codeing = utf-8 -*-
# @Time : 2021/8/17 15:17
# @Author : zyxiao
# @File : testXlwt.py
# @Software : {PyCharm}

import xlwt
'''
workbook=xlwt.Workbook(encoding="utg-8")   #创建Workbook对象
worksheet=workbook.add_sheet("sheet1")  #创建工作表
worksheet.write(0,0,"hello")   #在第一行第一列写入数据“hello”
workbook.save("info.xls")
'''


workbook=xlwt.Workbook(encoding="utg-8")   #创建Workbook对象
worksheet=workbook.add_sheet("sheet1")  #创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(j+1,i+1,(i+1)*(j+1)))
workbook.save("info.xls")