'''
通过用户输入日期判断是第几天
用列表代替元组
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
    #列出数列
    date_input = [31,28,31,30,31,30,31,31,30,31,30,31]
    if judge_year(year):
        date_input[1] = 29


    days = sum(date_input[:month - 1]) + day
    # judge_year(year)
    # if month > 2 and judge_year(year):
    #
    #         days += 1


    print('当前是第{}天'.format(days))
if __name__ == '__main__':
    main()