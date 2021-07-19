'''
2020/5/16
学习数据分析
'''

from matplotlib import pyplot as plt
import random
#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():
    #设置图形大小
    plt.figure(figsize=(20,8),dpi=80)


    a = ["青椒","土豆","西红柿","坦克"]
    b = [5,6,7,8]



    plt.bar(a,b,width = 0.1,color = "orange") #bar 条形图 barh 横着画 height  width

    plt.xticks(range(7),a,rotation=45)

    plt.xlabel("我爱吃的蔬菜")

    plt.show()
if __name__ == '__main__':
    main()