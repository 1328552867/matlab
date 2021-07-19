"""
2020/9/10
折腾文件名

"""
#引用os库
import os
#修改目录名 d：/tools/aaa 为d：/tool/bbb
os.rename("tmp/python/fileop","tmp/python/fileop")
# 修改文件名 d:/tools/first.py 为 d:/tools/second.py
os.rename('d:/tools/first.py','d:/tools/second.py')