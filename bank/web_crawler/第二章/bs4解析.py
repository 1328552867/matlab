#拿页面源代码
#使用bs4进行解析，拿到数据
import requests
import csv
from bs4 import BeautifulSoup
f = open("菜价.csv",mode="w",newline='')
csvwriter = csv.writer(f)
for i in range(1,10):
    url = 'http://www.xinfadi.com.cn/marketanalysis/0/list/'+str(i)+'.shtml'
    resp = requests.get(url)
    #解析数据
    #1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
    page = BeautifulSoup(resp.text,'html.parser')#指定html解析器
    #2.从bs对象中查找数据
    #find(标签，属性=值)
    #find_all(标签，属性=值)
    #table = page.find("table",class_="hq_table")#class是关键字
    table = page.find("table",attrs={"class":"hq_table"})#字典格式的值

    trs = table.find_all("tr")[1:]

    for tr in trs:#每一行
        tds = tr.find_all("td")
        name = tds[0].text#.text 表示拿到被标签标记的内容
        low  = tds[1].text
        avg  = tds[2].text
        high = tds[3].text
        gui  = tds[4].text
        kind = tds[5].text
        date = tds[6].text
        csvwriter.writerow([name,low,avg,high,gui,kind,date])

f.close()
resp.close()
print("over")







