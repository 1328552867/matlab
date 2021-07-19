"""
2020/8/26
学习xlrd
读取excel
"""
import xlrd

data=xlrd.open_workbook(r'S:\xlsx\123.xlsx')#打开excel文件  加r是为了防止字符转义

print(f"包含表单数量 {data.nsheets}")#
print(f"表单的名分别为: {data.sheet_names()}")#以列表的形式输出页签名

sheet2 = data.sheet_by_name('你好') #打开页签 通过sheet名称获取所需的sheet对象
nrows = sheet2.nrows #获取行数
ncols = sheet2.ncols #获取列数
print(nrows,ncols)#输出结果

cell_A = sheet2.cell(0,0).value#取出第一行第一列的值
print(cell_A)#输出结果
print(data.sheets())
sheet = data.sheet_by_index(0)
print(f"表单名：{sheet.name} ")
print(f"表单索引：{sheet.number}")
print(f"表单行数：{sheet.nrows}")
print(f"表单列数：{sheet.ncols}")
print(f"单元格A1内容是: {sheet.cell_value(rowx=0, colx=0)}")