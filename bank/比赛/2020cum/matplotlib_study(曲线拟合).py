
import xlrd
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d

#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():
    book = xlrd.open_workbook('C:\\Users\DELL\Desktop\D\\附件1_工件1的测量数据.xlsx')

    sheet = book.sheet_by_name("down")

    # for x,y in zip(range(1,sheet.nrows),range(1,sheet.ncols)):
    # if isinstance(sheet.cell_value(x, y), (int, float)):  # 判断数值类型
    #  pass
    # else:
    # print(1)

    x = sheet.col_values(colx=0, start_rowx=1)
    y = sheet.col_values(colx=1, start_rowx=1)

    # 设置图片大小
    plt.figure(figsize=(100, 100), dpi=80)  # figsize图片大小 dpi图片清晰度

    # 设置x轴的刻度
    # _xtick_labels = [i/2 for i in range(4,49)]
    # plt.xticks(_xtick_labels,rotation=45)#rotation旋转的度数
    '''
    x = range（0，120）
    list(x)[::10]类似于range（0,120,10）
    '''
    # 设置y轴刻的度
    # plt.yticks(range(min(y),max(y) + 1))

    # 绘制网格
    # plt.grid(alpha=0.4)

    # 添加描述信息
    plt.xlabel("这是x轴")
    plt.ylabel("这是y轴")
    plt.title("这是标题")

    plt.scatter(x, y)  # 绘制折线图

    plt.show()  # 展示图像
if __name__ == '__main__':
    main()
