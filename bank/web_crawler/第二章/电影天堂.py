#定位到2020必看片
#从2020必看片中提取到子页面的链接地址
#请求子页面的链接地址，拿到想要的下载地址
import re
import requests

domain = "https://www.dy2018.com/"
resp = requests.get(domain,verify=False)#verify=False去掉安全验证
resp.encoding = 'gb2312'#指定字符集
#print(resp.text)

obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)#预加载
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<mag>.*?")>magnet:',re.S)
result1 = obj1.finditer(resp.text)#应用预加载
child_href_list = []
for it in result1:
    ul = it.group('ul')

    #提取子页面链接：
    result2 = obj2.finditer(resp.text)
    for itt in result2:
        #拼接子页面的url地址：域名+子页面地址
        child_href = domain + itt.group('href').strip('/')
        child_href_list.append(child_href)#用列表保存子页面链接

#提取子页面内容
for href in child_href_list:
    resphref = requests.get(href, verify=False)  # verify=False去掉安全验证
    resphref.encoding = 'gb2312'  # 指定字符集
    result3 = obj3.finditer(resphref.text)
    for ittt in result3:
        print(ittt.group("name"))
        print(ittt.group("mag"))
        break






