#拿到页面源代码
#提取和解析数据
import requests
from lxml import etree
url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
html = etree.HTML(resp.text)
divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for div in divs:#每一个服务商信息
    div

resp.close()