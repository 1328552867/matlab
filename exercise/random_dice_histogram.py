'''
模拟两个骰子随机掷出
可视化图表（直方图）
'''

import random
import matplotlib.pyplot as plt

#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def roll_dice():#模拟骰子掷出
    roll = random.randint(1,6)
    return roll
def main():
    total_times = 10000#投掷次数

    #记录骰子结果
    roll_list = []


    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        # 记录骰子结果
        roll_list.append(roll1 + roll2)
    #数据可视化
    #设置直方图
    plt.hist(roll_list,bins=range(2,14),normed=1,edgecolor='black',linewidth=1)
    #直方图标题
    plt.title('骰子点数统计')
    #x轴
    plt.xlabel('点数')
    #y轴
    plt.ylabel('概率')
    plt.show

if __name__ == '__main__':
    main()








