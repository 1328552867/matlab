'''
模拟两个骰子随机掷出
可视化图表
'''

import random
import matplotlib.pyplot as plt

def roll_dice():#模拟骰子掷出
    roll = random.randint(1,6)
    return roll
def main():
    total_times = 100#投掷次数
    #初始化列表
    result_list = [0]*11


    #初始化点数列表
    roll_list = list(range(2,13))

    roll_dict = dict(zip(roll_list,result_list))#zip()将两个列表组合成元组
    #记录骰子结果
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        # 记录骰子结果
        roll1_list.append(roll1)
        roll2_list.append(roll2)


        for j in range(2,13):
            if (roll1 + roll2) == j :
                roll_dict[j] += 1
    for i,x in roll_dict.items():#遍历字典

        print('点数{}的次数{}概率为{}'.format(i,x,x / total_times))
    #数据可视化
    x = range(1,total_times + 1)
    plt.scatter(x,roll1_list,c='pink',alpha=0.5)
    plt.scatter(x, roll2_list,c='gold',alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()








