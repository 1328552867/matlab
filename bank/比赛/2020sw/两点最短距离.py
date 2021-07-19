# from collections import deque
# from collections import namedtuple
#
#
# def bfs(start_node, end_node, graph):
#     node = namedtuple('node', 'name, from_node')
#     search_stack = deque()  # 这里当作栈使用
#     name_search = deque()
#     visited = {}
#
#     search_stack.append(node(start_node, None))
#     name_search.append(start_node)
#     path = []
#     path_len = 0
#
#     print('开始搜索...')
#     while search_stack:
#         print('待遍历节点: ', name_search)
#         current_node = search_stack.pop()  # 使用栈模式，即后进先出，这是DFS的核心
#         name_search.pop()
#         if current_node.name not in visited:
#             print('当前节点: ', current_node.name, end=' | ')
#             if current_node.name == end_node:
#                 pre_node = current_node
#                 while True:
#                     if pre_node.name == start_node:
#                         path.append(start_node)
#                         break
#                     else:
#                         path.append(pre_node.name)
#                         pre_node = visited[pre_node.from_node]
#                 path_len = len(path) - 1
#                 break
#             else:
#                 visited[current_node.name] = current_node
#                 for node_name in graph[current_node.name]:
#                     if node_name not in name_search:
#                         search_stack.append(node(node_name, current_node.name))
#                         name_search.append(node_name)
#     print('搜索完毕,路径为:', path[::-1], "长度为:", path_len)  # 这里不再是最短路径，深度优先搜索无法一次给出最短路径
#
#
# if __name__ == "__main__":
#
#     graph = dict()
#     graph[1] = [3, 2]
#     graph[2] = [5]
#     graph[3] = [4, 7]
#     graph[4] = [6]
#     graph[5] = [6]
#     graph[6] = [8]
#     graph[7] = [8]
#     graph[8] = []
#     bfs(1, 8, graph)
import xlrd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

#修改字体解决中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def main():

    book = xlrd.open_workbook('C:\\Users\吴志豪\Desktop\\Attachment 1.xlsx')

    sheet_nodes = book.sheet_by_name("nodes")

    sheet_location = book.sheet_by_name("location")

    sheet_links = book.sheet_by_name("links")

    x = sheet_nodes.col_values(colx=1,start_rowx=1)
    y = sheet_nodes.col_values(colx=2,start_rowx=1)

    m = sheet_location.col_values(colx=1,start_rowx=2)
    n = sheet_location.col_values(colx=2,start_rowx=2)

    g = sheet_links.col_values(colx=0,start_rowx=1)
    h = sheet_links.col_values(colx=1,start_rowx=1)
    width = sheet_links.col_values(colx=2,start_rowx=1)

    #设置图片大小
    plt.figure(figsize=(100,100),dpi=80)#figsize图片大小 dpi图片清晰度

    #添加描述信息
    plt.xlabel("")
    plt.ylabel("")
    plt.title("")


    #定义储存D
    D = []
    #定义所有积雪点
    sn = [2,8,15,21,24,27,30,39,42,49,51,53,55,68,69,72,85,87,92,95,97,99,104,111,120,122,124,131,133,138]

    start = int(input('请输入初始位置')) - 1
    #经纬度
    start_site = (x[start],y[start])
    print(start_site)
    














if __name__ == '__main__':
    main()


























