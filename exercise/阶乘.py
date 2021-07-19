'''
2020/4/30
'''
import math
def main():
    m = 0
    for i in range(1,10):
        n =  math.factorial(i)  #求阶乘
        print('{}的阶乘为{}'.format(i,n))
        m = n + m
    print('和为{}'.format(m))
if __name__ == '__main__':
    main()