'''
2020/5/18
numpy数组的创建
'''

import numpy as np


a = np.arange(10)#类似range（10）函数，返回ndarray类型

b = np.ones((3,6))#生成一个纵3横6的全1矩阵

c = np.zeros((3,6))#生成一个纵3横6的全0矩阵

d = np.eye(5)#生成一个对角线为1其余为0的5×5矩阵

e = np.ones((2,3,4))#生成两个纵3横4的全1矩阵

f = np.ones_like(a)#根据数组a的形状生成一个全1数组

g = np.zeros_like(a)#根据数组a的形状生成一个全0数组

h = np.full_like(a,'val')#根据数组a的形状生成一个数组 每个元素值都是val

i = np.linspace()#根据起止数据等间距地填充数据，形成数组

j = np.concatenate()#将两个或多个数组合并成一个新的数组




print(a)
print('***********')
print(b)
print('***********')
print(c)
print('***********')
print(d)
print('***********')
print(e)

