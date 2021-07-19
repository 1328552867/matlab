'''
模拟骰子随机掷出
'''
import random
def roll_dice():
    roll = random.randint(1,6)
    return roll
def main():
    total_times = 10000#投掷次数
    #初始化列表[0,0,0,0,0,0]
    result_list = [0]*6

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1,7):
            if roll == j :
                result_list[j - 1] += 1
    for i,x in enumerate(result_list):#enumerate 返回序列在i上

        print('点数{}的次数{}概率为{}'.format(i+1,x,x / total_times))

if __name__ == '__main__':
    main()








