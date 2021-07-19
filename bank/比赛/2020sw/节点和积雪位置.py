import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():
    #打开工作簿
    book = xlrd.open_workbook('C:\\Users\DELL\Desktop\Attachment 1.xlsx')
    #读取表单
    sheet_nodes = book.sheet_by_name("nodes")
    sheet_location = book.sheet_by_name("location")
    sheet_links = book.sheet_by_name("links")

    x = sheet_nodes.col_values(colx=1,start_rowx=1)
    y = sheet_nodes.col_values(colx=2,start_rowx=1)

    m = sheet_location.col_values(colx=1,start_rowx=2)
    n = sheet_location.col_values(colx=2,start_rowx=2)

    g = sheet_links.col_values(colx=0,start_rowx=1)
    h = sheet_links.col_values(colx=1,start_rowx=1)
    width = sheet_links.col_values(colx=2,start_rowx=1)

    #设置图片大小
    plt.figure(figsize=(100,100),dpi=80)#figsize图片大小 dpi图片清晰度

    #添加描述信息
    plt.xlabel("")
    plt.ylabel("")
    plt.title("")
    #标记路口和潜在积雪位置
    plt.scatter(x, y, color='red')  # 绘制散点图
    plt.scatter(m, n, color='blue', marker='v', s=100)

    #plt.savefig("./t1.png")#保存图像 .svg 保存为矢量图
    #根据道路宽度画图
    i = []
    v = []
    wid = 0
    for i,v in zip(g,h) :
        i  = int(i)
        v  = int(v)

        #j=[x[i-1],y[i-1]]
        #f=[x[v-1],y[v-1]]
        j = [x[i-1],x[v-1]]
        f = [y[i-1],y[v-1]]
        if width[wid] == 2:

            print(j,f)
            plt.plot(j,f,color='green',linewidth = width[wid]/2  )
            wid = wid + 1
        elif width[wid] == 4:
            plt.plot(j, f, color='deepskyblue', linewidth=width[wid] / 2)
            wid = wid + 1

        elif width[wid] == 6:
            plt.plot(j, f, color='pink', linewidth=width[wid] / 2)
            wid = wid + 1

        else:
            plt.plot(j, f, color='y', linewidth=width[wid] / 2)
            wid = wid + 1

     #plt.plot((x[i],y[i]),(x[v],y[v]))

    plt.show() #展示图像

if __name__ == '__main__':
    main()