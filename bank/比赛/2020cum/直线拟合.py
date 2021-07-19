import xlrd

book = xlrd.open_workbook('C:\\Users\DELL\Desktop\D\\附件1_工件1的测量数据.xlsx')

sheet = book.sheet_by_name("level")

sum_x = sum(sheet.col_values(colx=0, end_rowx=6340,start_rowx=1))
sum_y = sum(sheet.col_values(colx=1, end_rowx=6340,start_rowx=1))
#求下x，y平均值
mean_x = sum_x/(6340)
mean_y = sum_y/(6340)
sx = 0
sy = 0

for xi,yi in zip(sheet.col_values(colx=0, start_rowx=6340),sheet.col_values(colx=1, start_rowx=6340)):

    sx = sx + (xi-mean_x)*(yi-mean_y)
    sy = sy + (xi-mean_x)*(xi-mean_x)

    b = sx/sy
    a = mean_y - b*mean_x

    Lyy = (yi-mean_y)*(yi-mean_y)
    Q = (yi-b*xi+a)*(yi-b*xi+a)
    R2 = 1-Q/Lyy
print(a,b,R2)
