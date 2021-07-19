"""
2020/8/9
数据处理 饼图
1图像大小
2饼图分离
3设置正圆
4添加图例
"""
import matplotlib.pyplot as plt

#解决中文乱码问题

# 正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus']=False

#刻度的大小
plt.rcParams['axes.labelsize'] = 16

#线的粗细
plt.rcParams['lines.linewidth'] = 2

#x轴的大小
plt.rcParams['xtick.labelsize'] = 14
#y轴的大小
plt.rcParams['ytick.labelsize'] = 14

#图例大小
plt.rcParams['legend.fontsize'] = 14

#图的大小
plt.rcParams['figure.figsize'] = [12,8]
#=======================================#基本的使用实例
#定义饼的标签，
labels = ['菠萝','12','#￥','E']

#每个标签所占的比例
x  = [25,25,25,25]

#饼图分离 分别对应四个变量离中心的程度
explode = (0,0.1,0,0)

#显示百分比#绘制饼图
#textprops={'fontsize':18,'color':'k'} 设置为字体大小为18，颜色黑色
plt.pie(x,labels=labels
        ,autopct='%3.2f%%'
        ,textprops={'fontsize':18,'color':'k'}
        ,explode=explode
        ,shadow=True)#添加阴影

#设置x,y的刻度一样，使其饼图为正圆
plt.axis('equal')
#添加图例
plt.legend()

# 标题
plt.title('2020年饼图测试',fontsize=20)

plt.show()