'''
通过用户输入日期判断是第几天

'''
from datetime import  datetime

def main ():
    date_input = input('请输入日期(yyyy/mm/dd)')
    date = datetime.strptime(date_input, '%Y/%m/%d')
    days = date.strftime('%j')



    print('当前是第{}天'.format(days))
if __name__ == '__main__':
    main()