'''
判断密码强弱
循环终止
添加储存密码的文本文件
'''

def check_number_exist(password_str):
    #判断字符串中是否含有数字
    has_number = False      #分辨循环是满足条件退出还是执行完退出
    for c  in password_str:
        if c.isnumeric():
            has_number = True
            break
    return  has_number

def check_letter_exist(password_str):
    #判断字符串中是否含有字母
    has_letter = False
    for c  in password_str:
        if c.isalpha():
            has_letter = True
            break
    return  has_letter


def main():
    #尝试次数
    try_time = 5
    while try_time > 0:

        password = input('请输入密码：')

        #密码强度
        strength_level = 0

        #规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位')
        # 规则2：密码要求包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则3：密码要求包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')

        if strength_level < 3 :
            print('密码强度不够')
            try_time -= 1
            print()
        else:
            print('恭喜，密码合格！')

        if strength_level == 1 :
            level = '弱'
        elif strength_level == 2 :
            level = '中'
        else:
            level = '强'

        f = open('password_3.0.txt', 'a')#创建文本文件 'a'意为在继续添加
        f.write('密码:{}，强度:{}\n'.format(password,level))#写入
        f.close()#关闭
        #explorer 打开资源管理器

    print('尝试次数过多,密码设置失败！')


if __name__ == '__main__':
    main()
