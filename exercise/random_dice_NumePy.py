'''
模拟两个骰子随机掷出
可视化图表（直方图）
'''


import matplotlib.pyplot as plt
import numpy as np


#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False


def main():
    total_times = 10000#投掷次数

    #记录骰子结果
    roll1_arr = np.random.randint(1,7,size=total_times)
    roll2_arr = np.random.randint(1,7, size=total_times)
    result_arr = roll1_arr + roll2_arr


    list,bins = np.histogram(result_arr,bins=range(2,14))
    print(list)
    print(bins)

    #数据可视化
    #设置直方图
    plt.hist(result_arr,bins=range(2,14), density=1,edgecolor='black',linewidth=1,rwidth=0.8)
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    #x轴显示
    plt.xticks(tick_pos,tick_labels)


    #直方图标题
    plt.title('骰子点数统计')
    #x轴标题
    plt.xlabel('点数')
    #y轴标题
    plt.ylabel('概率')
    plt.show()

if __name__ == '__main__':
    main()








