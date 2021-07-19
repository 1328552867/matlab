import  xlrd
"获取12个月的文件名字"
for i in range(1,13):
    #迭代1-12
    if i <= 9:
        str_path = "C:\\Users\吴志豪\Desktop\CUMCM-2016D\CUMCM2016-D-Appendix-Chinese\附件1  平均风速和风电场日实际输出功率表\\20150"+str(i)+".xls"
    else:
        str_path = "C:\\Users\吴志豪\Desktop\CUMCM-2016D\CUMCM2016-D-Appendix-Chinese\附件1  平均风速和风电场日实际输出功率表\\2015" + str(i) + ".xls"
    print(str_path)
    "打开所有工作簿"
    book = xlrd.open_workbook(str_path)

    for n in book.sheet_names():
        #迭代所有表单名
        sheet_a = book.sheet_by_name(n)
        print(f"表单名：{sheet_a.name} ")
        for m in range(3,sheet_a.nrows):
            for j in range(sheet_a.ncols):
                #遍历列行
                if isinstance(sheet_a.cell_value(m,j),(int,float)):#判断数值类型
                    pass
                else:
                    print(1,m,j)
    # 将所有风速放入一个列表中再求和
    book_a = xlrd.open_workbook("C:\\Users\吴志豪\Desktop\CUMCM-2016D\CUMCM2016-D-Appendix-Chinese\附件1  平均风速和风电场日实际输出功率表\\201501.xls")
    sheet_b = book_a.sheet_by_name('Sheet1')
    wind_speed_1 = sheet_b.col_values(colx=2, start_rowx=3)
    wind_speed_2 = sheet_b.col_values(colx=5, start_rowx=3)
    wind_speed_3 = sheet_b.col_values(colx=8, start_rowx=3)
    wind_speed_4 = sheet_b.col_values(colx=11, start_rowx=3)
    wind_speed = wind_speed_1 + wind_speed_2 + wind_speed_3 + wind_speed_4
    print(wind_speed)
    sum1 = sum(wind_speed)
    print(sum1/96)


