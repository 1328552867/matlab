import math
from sympy import *
from sympy.abc import x,y,a,b,c

x0,y0,x1,y1 = input('请输入两点坐标以空格隔开').split()
x0 = float(x0)
y0 = float(y0)
x1 = float(x1)
y1 = float(y1)

x2 = 2*x0-x1
y2 = y1

k1 = (y1-y0)/(x1-x0)
k2 = (y2-y0)/(x2-x0)

mx1 = (x0+x1)/2
my1 = (y0+y1)/2
mx2 = (y0+x2)/2
my2 = (y0+y2)/2

mk1 = -1/k1
mk2 = -1/k2
#圆心坐标
mxy = solve([y-my1-k1*(x-mx1),y-my2-k2*(x-x2)],[x,y])
xr = mxy[x]
yr = mxy[y]


