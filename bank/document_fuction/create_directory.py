"""
2020/9/9
文件与文件目录的创建删除拷贝
"""
#引用os库
import os
#os.makedirs 创建目录结构
#exist_ok=true 指定了，如果某个要创建的目录已经存在，也不报错
os.makedirs("tmp/python/fileop",exist_ok=True)

#os.remove 删除一个文件
#os.remove("")

#shutil.rmtree() 可以递归的删除某个目录所有的子目录和子文件

#import shutil
#shutil.rmtree("C:\\Users\\吴志豪\\Desktop\\lajidaima\\PY\\bank\\document_fuction\\tmp")

#拷贝文件
#from shutil import copyfile
# 拷贝 d:/tools/first.py 到 e:/first.py
#copyfile('d:/tools/first.py', 'e:/first.py')

#拷贝目录
#from shutil import copytree
# 拷贝 d:/tools/aaa 目录中所有的内容 到 e:/bbb 中
#copytree('d:/tools/aaa', 'e:/new/bbb')

