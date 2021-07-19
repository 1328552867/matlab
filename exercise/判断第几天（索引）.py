'''
通过用户输入日期判断是第几天
区间索引形式
'''


def main ():
    date_input = input('请输入日期(yyyy/mm/dd)')
    year_str = date_input[0:4]
    month_str = date_input[5:7]
    day_str = date_input[8:]

    year = int(year_str)
    month = int(month_str)
    day = int (day_str)

    days = 0

    date_input = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 400 == 0 ) or ((year % 4 == 0)and(year % 100 != 0)):
        date_input[1] = 29

    days = sum(date_input[:month - 1]) + day
    print('当前是第{}天'.format(days))
if __name__ == '__main__':
    main()