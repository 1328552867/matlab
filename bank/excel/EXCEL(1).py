"""
2020/9/6
打开“数据处理素材.xlsx”
求第一页签所有品牌各个月销售总和于平均

"""
"引入xlrd库"
import xlrd
"打开文件"
book = xlrd.open_workbook(r'C:\Users\吴志豪\Desktop\你不需要知道\wxp\数据处理素材.xlsx')
"输出该文件表单数量以及名称"
print(f"包含表单数量 {book.nsheets}")
print(f"表单的名分别为: {book.sheet_names()}")
"表单索引从0开始，获取第一个表单对象"
sheet = book.sheet_by_index(0)
"获取列表形式的各个月销售"
market =  sheet.row_values(rowx=2,start_colx=2)
"求和"

print(market)

