from matplotlib import pyplot as plt
#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():
    x = [1,2,3,4,5,9,9,9]
    y = [5,4,3,2,1,9,9,9]

    plt.xticks(range(1,100,20),range(1,100))


    plt.plot(x,y)




    plt.show()
if __name__ == '__main__':
    main()