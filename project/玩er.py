import os, sys
def mkdir():
    path = 'C:\\'#创建文件路径
    i = 0
    a = 1
    while a>0: #创建文件个数
        file_name = path + str(oct(i))
        os.mkdir(file_name)
        i=i+1
mkdir()