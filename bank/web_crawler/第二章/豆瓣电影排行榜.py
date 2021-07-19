#拿取页面源代码
#通过re来提取想要的有效信息
import requests
import re
import csv
headers ={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
f = open("data.csv",mode="w",encoding="utf-8",newline="")
for i in range(0,250,25):
    url = "https://movie.douban.com/top250?start="+ str(i)
    resp = requests.get(url,headers=headers)
    page_content = resp.text#将获取到的网页转换为text文件赋值
    #解析数据
    #预加载正则表达式
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<br>(?P<year>.*?)&nbsp'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*? <span property="v:best" content="10.0"></span>.*?<span>'
                     r'(?P<num>.*?)</span>',re.S)
    result = obj.finditer(page_content)
    #创建csv文件


    csvwriter = csv.writer(f)
    for it in result:
        # print(it.group("name"))
        # print(it.group("year").strip())#.strip()移除字符串前后指定的内容 默认是空格
        # print(it.group("score")+"分")
        # print(it.group("num"))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
f.close()
print("over")
resp.close()

