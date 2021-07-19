#regular expression正则表达式
"""
常用元字符：
.  匹配除换行符以外的任意字符
\w 匹配字母或数字或下划线
\s 匹配任意的空白符
\d 匹配数字
\n 匹配一个换行符
\t 匹配一个制表符

^ 匹配字符串的开始
$ 匹配字符串的结尾

\W  匹配非字母或数字或下划线
\D  匹配非数字
\S  匹配非空白符
a|b 匹配字符a或字符b
()  匹配括号内的表达式，也表示一个组
[...]  匹配字符组中的字符
[^...] 匹配除了字符组中字符的所有字符
"""
"""
量词：控制前面的元字符出现的次数
*   重复零次或更多次
+   重复一次或更多次
？   重复零次或一次
{n}   重复n次
{n,}  重复n次或更多次
{n,m} 重复n次到m次    
贪婪匹配和惰性匹配
.*    贪婪匹配
.*?   惰性匹配
"""
import re
# #findall：匹配字符串中所有的符合正则的内容
# lst = re.findall(r"\d+","我的电话是：10086,我女朋友电话是10010")
# print(lst)
#
# #finditer：匹配字符串中所有的内容，（返回的是迭代器），从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+","我的电话是：10086,我女朋友电话是10010")
# for i in it:
#     print(i.group())

# #search找到一个结果就返回，（返回的是match对象），拿到内容需要.group()
# s = re.search(r"\d+","我的电话是：10086,我女朋友电话是10010")
# print(s.group())

# #march是从头开始匹配
# s = re.match(r"\d+","我的电话是：10086,我女朋友电话是10010")
# print(s.group())

# #预加载正则表达式
# obj = re.compile(r"\d+")
#
# ret = obj.finditer("我的电话是：10086,我女朋友电话是10010")
# for i in ret:
#      print(i.group())
#
# ret = obj.findall("我今天吃了一份5000元的牛排，太爽了！")
# print(ret)

s =""""
<div class='jay'><span id='1'>凌美</span></div>
<div class='jj'><span id='2'>百乐</span></div>
<div class='jolin'><span id='3'>白金</span></div>
<div class='sylar'><span id='4'>万宝龙</span></div>
<div class='tory'><span id='5'>写乐</span></div>
"""
#(?P<分组名字>正则)可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<name>.*?)</span></div>",re.S)#re.S 让.能匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group('name'))#从name中拿取
    print(it.group())








