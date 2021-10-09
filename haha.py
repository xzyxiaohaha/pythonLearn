# -*- codeing = utf-8 -*-
# @Time : 2021/10/8 16:13
# @Author : zyxiao
# @File : haha.py
# @Software : {PyCharm}
import xlrd
import xlwt
book = xlrd.open_workbook('nameList.xlsx')  # 源excel文件
sheet = book.sheet_by_index(1)  # 表示第几个sheet
workbook = xlwt.Workbook(encoding='utf-8')  # 输出的excel文件编码格式

worksheet = workbook.add_sheet('2019')  # 输出的sheet名字
index = 0
print(sheet.ncols)
for i in range(0, sheet.ncols):  # sheet.ncols表示一个sheet中的列数，2019年的sheet中一共有2107列
    cell = sheet.cell(0, i)  # 获取第0行，第1 2 3 4 ......2107列单元格
    if i % 7 == 0 and i != 0:  # 因为每7列一个重复，基于此设置i%7==0的判断条件，也就是每遍历7个单元格，就把index+1
        index += 1
    worksheet.write(index, i % 7, label=cell.value)  # 将数据放到对应的单元格中
workbook.save('newNameList.xls')  # 保存，并设置输出的文件名