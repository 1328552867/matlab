#实现功能：根据用户输入日期，返回该周存款金额

import math
import datetime


def save_money_in_n_weeks (money_per_week,increase_week,toral_week):
    money_list = []  # 记录每周存款数列表
    money_week_list = []  #记录该周存款金额
    for i in range(toral_week):
        #存钱操作
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        #print('第{}周，存入{}元，账户累计{}元'.format(i + 1,money_per_week,saving))
        #更新下一周的存钱金额
        money_per_week += increase_week
        money_week_list.append(saving)#更新列表
    return  money_week_list

def main():
    money_per_week = float(input('请输入每周的存入的金额'))  # 每周的存入金额
    increase_week = float(input('请输入每周的递增金额'))  # 递增的金额
    toral_week = int(input('请输入想存多少周'))  # 总共的周数
    input_data_str = input('请输入日期（yyyy/mm/dd：）')
    input_data = datetime.datetime.strptime(input_data_str,'%Y/%m/%d')#转化格式
    week_num = input_data.isocalendar()[1] #第几周
    money_week_list = save_money_in_n_weeks(money_per_week, increase_week, toral_week)#将函数中的列表赋值出来
    print(input_data)
    print('第{}周总金额为{}'.format(week_num,money_week_list[week_num - 1]))
if __name__ == '__main__':
    main()
