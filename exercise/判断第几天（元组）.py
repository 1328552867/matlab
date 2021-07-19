'''
通过用户输入日期判断是第几天
元组
'''
from datetime import  datetime

def main ():
    date_input = input('请输入日期(yyyy/mm/dd)')
    date = datetime.strptime(date_input,'%Y/%m/%d')
    year = date.year
    month = date.month
    day = date.day
    #列出元组
    date_input = (31,28,31,30,31,30,31,31,30,31,30,31)

    days = sum(date_input[:month - 1]) + day
    if (year % 400 == 0 ) or ((year % 4 == 0)and(year % 100 != 0)):
        if month > 2 :
            days += 1


    print('当前是第{}天'.format(days))
if __name__ == '__main__':
    main()