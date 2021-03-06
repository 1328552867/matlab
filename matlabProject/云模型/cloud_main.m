% 4组选手的60发气步枪成绩
% 分析选取一位发挥最出色的选手

clc;
clear all;
close all;
% 每幅图生成N个云滴
N = 1500;
% 射击成绩的原始数据
Y = [
    9.5 10.3 10.1 8.1;
    10.3 9.7 10.4 10.1;
    10.6 8.6 9.2 10.0;
    10.5 10.4 10.1 10.1;
    10.9 9.8 10.0 10.1;
    10.6 9.8 10.0 10.1;
    10.4 10.5 10.6 10.3;
    10.1 10.2 10.8 8.4;
    9.3 10.2 9.6 10.0;
    10.5 10.0 10.7 9.9;
    ];

for i = 1: size(Y,2)
% size(A,dim)
% 当dim:1 时，表示返回行数
% 当dim:2时，表示返回列数
% 当dim:3时，表示返回页数
    subplot(size(Y,2)/2, 2, i)
% subplot（m,n,p）
% subplot是将多个图画到一个平面上的工具。
% 其中，m表示是图排成m行，n表示图排成n列，
% 如果m=2就是表示2行图。
% p表示图所在的位置，p=1表示从左到右从上到下的第一个位置。
    % 调用函数
    [x, y, Ex, En, He] = cloud_compute(Y(:,i), N);%Y(:,i)输出Y矩阵第i列全部数据
    plot(x, y, 'r.');
    xlabel('射击成绩分布/环');
    ylabel('确定度');
    title('人射击云模型还原图谱');
    % 控制坐标轴的范围
    % 统一坐标轴上才会在云模型形态上才具有可比性
    axis([8, 12, 0, 1]);
%    坐标设置 axis([xmin xmax ymin ymax])
end



