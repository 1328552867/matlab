'''
2020/5/16
学习数据分析
'''

from matplotlib import pyplot as plt
import random
#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():
    #设置图形大小
    plt.figure(figsize=(20,8),dpi=80)

    a = [98,126,99,56,5,6]

    plt.hist(a,1)



    plt.show()
if __name__ == '__main__':
    main()