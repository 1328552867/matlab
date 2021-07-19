hours = 1:12;%生成一个1到12的行向量
temps = [5 8 9 15 25 29 31 30 22 25 27 24];
h = 1:0.1:12;%生成一个步长为0.1的1到12的行向量
t = interp1(hours,temps,h,'spline');
%yi= interp1(x,y,xi,'method')  
%x，y为插值点，yi为在被插值点xi处的插值结果；x,y为向量，
plot(hours,temps,'+',h,t,hours,temps,'r:');%画多个图
xlabel('Hour'),ylabel('Degrees Celsius');
 

x = 1:5;
y = 1:3;
temps = [82 81 80 82 84;79 63 61 65 81;84 84 82 85 86];
mesh(x,y,temps);%画一个三维网格图
xi = 1:0.2:5;
yi = 1:0.2:3;
zi = interp2(x,y,temps,xi',yi,'cubic');
% ZI = interp2(X,Y,Z,XI,YI)
% X,Y 对应插值前X轴和Y轴的坐标分量，合在一起才是(x,y)
% Z是X，Y坐标对应位置（x,y）的值，XI,YI对应插值后的坐标。
mesh(xi,yi,zi);

p = polyfit(hours,temps,3);
xi = 1:0.1:12;
yi = polyval(p,xi);
plot(xi,yi,hours,temps,'r*');

[x,y] = meshgrid(1:10);
h = [0,0.02,-0.12,0,-2.09,0,-0.58,-0.08,0,0;
    0.02,0,0,-2.38,0,-4.96,0,0,0,-0.1;
    0,0.1,1,0,-3.04,0,-0.53,0,0.1,0;
    0,0,0,3.52,0,0,0,0,0,0;
    -0.43,-1.98,0,0,0,0.77,0,2.17,0,0;
    0,0,-2.29,0,0.69,0,2.59,0,0.3,0;
    -0.09,-0.31,0,0,0,4.27,0,0,0,-0.01;
    0,0,0,5.13,7.4,0,1.89,0,0.04,0;
    0.1,0,0.58,0,0,1.75,0,-0.11,0,0;
    0,-0.01,0,0,0.3,0,0,0,0,0.01];
[xi,yi]=meshgrid(1:0.1:10);%生成网格矩阵
hi = interp2(x,y,h,xi,yi,'spline');%二维插值命令
surf(hi);%画一个曲面图
xlabel('x'),ylabel('y'),zlabel('h');
