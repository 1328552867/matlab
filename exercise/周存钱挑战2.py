#for循环与math库的使用
import math

def save_money_in_n_weeks (money_per_week,increase_week,toral_week):
    money_list = []  # 记录每周存款数列表


    for i in range(toral_week):
        #存钱操作
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        #print('第{}周，存入{}元，账户累计{}元'.format(i + 1,money_per_week,saving))
        #更新下一周的存钱金额
        money_per_week += increase_week
    return  saving
def main():
    money_per_week = float(input('请输入每周的存入的金额'))  # 每周的存入金额

    increase_week = float(input('请输入每周的递增金额'))  # 递增的金额
    toral_week = int(input('请输入想存多少周'))  # 总共的周数


    saving = save_money_in_n_weeks(money_per_week, increase_week, toral_week)
    print('总金额为', saving)
if __name__ == '__main__':
    main()
