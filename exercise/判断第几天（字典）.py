'''
通过用户输入日期判断是第几天
学习集合
'''
from datetime import  datetime
#引入datetime包里的datetime类
def judge_year (year):
    '''
    如果是平年输出False
    如果是闰年输出True
    '''
    judge = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        judge = True
    return judge

def main ():
    date_input = input('请输入日期(yyyy/mm/dd)')
    date = datetime.strptime(date_input,'%Y/%m/%d')
    year = date.year
    month = date.month
    day = date.day
    #包含三十天月份集合
    # _30_days_month_set = {4,6,9,11}
    # _31_days_month_set = {1,3,5,7,8,10,12}
    month_day_dict = {1:31,
                      2:28,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}

    #初始化值
    days = 0
    days += day
    for i in range(1,month):#得到（1，2，...，month - 1）
        days += month_day_dict[i]#提取天数


        if judge_year(year) and month > 2:
            days += 1


    # days = sum(date_input[:month - 1]) + day
    # judge_year(year)
    # if month > 2 and judge_year(year):
    #
    #         days += 1


    print('当前是第{}天'.format(days))
if __name__ == '__main__':
    main()