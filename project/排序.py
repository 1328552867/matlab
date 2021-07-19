
import xlrd
from xlutils.copy import copy
#读取excel表
book1 = xlrd.open_workbook("C:\\Users\\13285\Desktop\\a.xls")
book2 = copy(book1)#拷贝一份原来的excel
sheet1 = book1.sheet_by_index(0)
sheet2 = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
i = 0
x = 0
while i <= sheet1.nrows-1:
    #获得每行每列的值
    C = sheet1.cell_value(rowx=i, colx=2)
    D = sheet1.cell_value(rowx=i, colx=3)
    E = sheet1.cell_value(rowx=i, colx=4)
    F = sheet1.cell_value(rowx=i, colx=5)
    G = sheet1.cell_value(rowx=i, colx=6)

    if C == '正确' or C == '错误':
        sheet2.write(x, 0, '判断题')
    elif len(G) == 1:
        sheet2.write(x, 0, '单选题')
        #列表排序
        aList = [C,D,E,F];
        aList.sort();

        sheet2.write(x, 2,aList[0])
        sheet2.write(x, 3,aList[1])
        sheet2.write(x, 4,aList[2])
        sheet2.write(x, 5,aList[3])
    else:
        sheet2.write(x, 0, '多选题')
        aList = [C, D, E, F];
        aList.sort();

        sheet2.write(x, 2, aList[0])
        sheet2.write(x, 3, aList[1])
        sheet2.write(x, 4, aList[2])
        sheet2.write(x, 5, aList[3])
    i = i + 1
    x = x + 1

book2.save("C:\\Users\\13285\Desktop\\a.xls")