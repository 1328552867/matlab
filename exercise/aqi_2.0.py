'''
AQI计算
'''

def cal_linear(iaqi_lo,iaqi_hi,bp_lo,bp_hi,cp):
    '''
        范围缩放
    '''
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo)/(bp_hi - bp_lo) + iaqi_lo
    return iaqi
def cal_pm_iaqi(pm_val):
    '''
        计算PM2.5AQI
    '''
    if 0 <= pm_val < 3:
        iaqi = cal_linear(0,50,0,3,pm_val)
    elif 3 <= pm_val < 5:
        iaqi = cal_linear(50,100,2,4,pm_val)
    else:
        pass

def cal_co_iaqi(co_val):
    '''
        计算COAQI
    '''
    if 0 <= co_val < 36:
        iaqi = cal_linear(0,50,0,35,co_val)
    elif 36 <= co_val < 76:
        iaqi = cal_linear(50,100,35,75,co_val)
    elif 76 <= co_val < 116:
        iaqi = cal_linear(100,150,75,115,co_val)
    else:
        pass
def cal_aql(param_list):
    '''
    AQL计算
    '''
    pm_val = param_list[0]
    co_val = param_list[1]



    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)
    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi


def main():
    print('请输入以下信息，用空格分割')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split('')#分割空格
    #接收PM2.5的值
    pm_val = float(str_list[0])
    #接收CO的值
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    #调用AQL计算函数
    aqi_val = cal_aql(param_list)

    print('空气质量指数为：{}'.format())

if __name__ == '__main__':
    main()










