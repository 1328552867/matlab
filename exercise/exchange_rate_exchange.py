
"""
    功能：汇率兑换
    时间：12/20
    版本1.0

"""
rmb_str_value = input('请输入人民币（CNY）金额:')

rmb_str_value = eval(rmb_str_value)
#将rmb_str_value由字符串转换为数字格式并赋值给rmb_str_value
USD_VS_RMB = 6.77

usd_value = rmb_str_value / USD_VS_RMB

print('美元（USD）的金额是',usd_value)

