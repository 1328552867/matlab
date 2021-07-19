import math

try:
    a = eval(input('请输入第一条边的边长'))
    b = eval(input('请输入第二条边的边长'))
    c = eval(input('请输入第三条边的边长'))
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    # :.2f 指保留两位小数
    print('三角形的面积是{:.2f}'.format(s))
except NameError:
    print('请输入正确数值')