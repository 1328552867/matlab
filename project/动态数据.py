from matplotlib import animation
from matplotlib import pyplot
from pylab import mpl
import math

mpl.rcParams['font.sans-serif'] = ["SimHei"]
mpl.rcParams['axes.unicode_minus'] = False
fig, ax = pyplot.subplots()  # 返回一个包含figure和axes对象的元组，将元组分解为fig和ax两个变量


def graph(num):
    ax.clear()  # 清除，不叠加
    if num < 50:
        ax.barh(1, num - 1, color='#adb0ff')  # 绘制水平方向的条形图barh()
        ax.text(num - 1, 1, "广东省", size=14, weight=600, ha='right', va='bottom')  # 添加文字并设置样式
        ax.barh(3, num + 0.1, color='#ffb3ff')
        ax.text(num + 0.1, 3, "北京省", size=14, weight=600, ha='right', va='bottom')
    if num >= 50:
        ax.barh(1, 50, color='#adb0ff')  # 绘制水平方向的条形图barh()
        ax.text(50, 1, "广东省", size=14, weight=600, ha='right', va='bottom')  # 添加文字并设置样式
        if num < 70:
            ax.barh(3, num + 2, color='#ffb3ff')
            ax.text(num + 2, 3, "北京省", size=14, weight=600, ha='right', va='bottom')
        if num >= 70:
            ax.barh(3, num - 1, color='#ffb3ff')
            ax.text(num - 1, 3, "北京省", size=14, weight=600, ha='right', va='bottom')
    ax.barh(5, num / math.tan(1), color='#90d595')
    ax.text(num / math.tan(1), 5, "云南省", size=14, weight=600, ha='right', va='bottom')
    pyplot.title('人口工作情况对比')  # 添加图标题


animator = animation.FuncAnimation(fig, graph, frames=range(1, 100), interval=1)
pyplot.show()  # 移动到函数外面，不然不会动态显示
