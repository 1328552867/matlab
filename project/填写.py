
import xlrd
from xlutils.copy import copy
#读取excel表
book1 = xlrd.open_workbook("C:\\Users\\13285\Desktop\\题目导入模板(汇总).xls")
book3 = xlrd.open_workbook("C:\\Users\\13285\Desktop\\模板1：试题导入模板.xls")
book2 = copy(book3)#拷贝一份原来的excel
sheet1 = book1.sheet_by_index(0)
sheet2 = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
i = 0
x = 0
while i <= sheet1.nrows-3:
    #获得每行每列的值
    C = sheet1.cell_value(rowx=i+2, colx=1)#题干
    D = sheet1.cell_value(rowx=i+2, colx=2)#题型
    E = sheet1.cell_value(rowx=i+2, colx=5)#答案
    F = sheet1.cell_value(rowx=i+2, colx=7)#A
    G = sheet1.cell_value(rowx=i+2, colx=8)#B
    H = sheet1.cell_value(rowx=i+2, colx=9)#C
    I = sheet1.cell_value(rowx=i+2, colx=10)#D
    J = sheet1.cell_value(rowx=i+2, colx=11)#E
    K = sheet1.cell_value(rowx=i+2, colx=12)#F
    L = sheet1.cell_value(rowx=i+2, colx=13)#G
    M = sheet1.cell_value(rowx=i+2, colx=14)#H
    N = sheet1.cell_value(rowx=i+2, colx=15)#I
    XU = x + 1
    O = "2"
    P = "常识"
    Q = "简单"
    sheet2.write(x + 1, 0,D)
    sheet2.write(x + 1, 1,C)
    sheet2.write(x + 1, 2,F)
    sheet2.write(x + 1, 3,G)
    sheet2.write(x + 1, 4,H)
    sheet2.write(x + 1, 5,I)
    sheet2.write(x + 1, 6,J)
    sheet2.write(x + 1, 7,E)
    sheet2.write(x + 1, 8,O)
    sheet2.write(x + 1, 9,P)
    sheet2.write(x + 1, 10,Q)
    sheet2.write(x + 1, 11,XU)

    i = i + 1
    x = x + 1

book2.save("C:\\Users\\13285\Desktop\\aDS.xls")