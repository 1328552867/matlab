'''
2020/4/27
'''

import random
import matplotlib.pyplot as plt
import numpy as np

def main():
    def bubbleSort(nums):
        for i in range(len(nums) - 1):  # 冒泡排序进行的趟数
            for j in range(len(nums) - i - 1):  # ｊ为列表下标
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]# 交换位置
        return nums

    nums = [random.randint(1,100)for i in range(200)]
    even_number = []#偶数
    odd_number = []#奇数
    l = bubbleSort(nums)
    for i in tuple(l):
        if i%2 == 1:
            odd_number.append(i)
        else:
            even_number.append(i)
    n = len(odd_number)- len(even_number)#列表个数
    if n > 0:#平衡列表元素个数
        for x in range(abs(n)):
            odd_number.pop(len(even_number))
    elif n < 0:
        for x in range(abs(n)):
            even_number.pop(len(odd_number))
    else:pass
    plt.hist(even_number,bins=len(even_number),range=(0,100),edgecolor='black',linewidth=0.5)



    plt.show()
if __name__ == '__main__':
    main()