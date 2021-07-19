import math
from sympy import *
from sympy.abc import x,y,a,b,c
#拐点坐标
x1 =1
y1 =1
#第二点
x2 =1
y2 =1
#圆心坐标
xr =1
yr =1
#圆的半径
r =1

k = (y2-y1)/(x2-x1)
b = (-x1*y2+x1*y2+y1*y2-y1*y1)/(x2-x1)

mxy = solve([y-k*x-b,y+(x-xr)/k+yr],[x,y])

mx = mxy[x]
my = mxy[y]

l = math.degrees((math.atan(((yr-my))/r)*math.pi*r*r)/360)

print(l)








