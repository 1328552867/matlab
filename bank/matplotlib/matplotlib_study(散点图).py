'''
2020/5/15
学习数据分析
'''

from matplotlib import pyplot as plt
import random
#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():
    y_3 = [random.randint(10,30) for _ in range(30) ]#随机生成30个10-29的数
    y_10 =[random.randint(10,30) for _ in range(30) ]

    x_3 = range(1,31)
    x_10 = range(51,81)
    #绘制散点图
    plt.figure(figsize=(20,8),dpi=80)

    plt.scatter(x_3,y_3)
    plt.scatter(x_10,y_10)

    plt.show()
if __name__ == '__main__':
    main()