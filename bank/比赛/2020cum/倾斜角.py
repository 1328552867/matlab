import math
for i in range(100):

    x1,y1,x2,y2 = input('请输入两点坐标以空格隔开').split()
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    k = (y2-y1)/(x2-x1)
    b = (-x1*y2+x1*y2+y1*y2-y1*y1)/(x2-x1)
    x = math.degrees(math.atan(k))
    print('直线方程为y={}x+{}'.format(k, b))
    print(x)



