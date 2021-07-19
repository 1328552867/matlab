
"""
    功能：汇率转换
    时间：12/20
    版本1.0
"""
USD_VS_RMB = 6.77
currency_str_value = input('请输入带单位的货币金额:')
danwei = currency_str_value[-3:]
print(danwei)


rmb_str_value = eval(currency_str_value)
#将rmb_str_value由字符串转换为数字格式并赋值给rmb_str_value


usd_value = rmb_str_value / USD_VS_RMB

print(currency_str_value)

