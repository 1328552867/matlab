

def main ():
    money_per_week = 10 #每周的存入金额
    i = 1               #记录周数
    increase_week = 10  #递增的金额
    toral_week = 52     #总共的周数
    saving = 0          #账户累计

    while i <= 52 :
        #存钱操作
        saving += money_per_week
        print('第{}周，存入{}元，账户累计{}元'.format(i,money_per_week,saving))
        money_per_week += increase_week
        i += 1

if __name__ == '__main__':
    main()
