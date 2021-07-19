#拿到主页面的源代码。然后提取到子页面的链接地址
#拿到子页面的内容。从子页面中找到图片的下载地址
#下载图片
import requests
from bs4 import BeautifulSoup
import time
url = "https://www.umei.net/bizhitupian/diannaobizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"

#把源代码交给bs
main_page = BeautifulSoup(resp.text,"html.parser")
alist = main_page.find("div",class_="TypeList").find_all("a")#把范围第一次缩小

url_href_list=[]
for a in alist:
    urlhref = url + a.get("href")[-10:]#直接通过get就能拿到属性值
    url_href_list.append(urlhref)


for href in url_href_list:
    resp_href = requests.get(href)
    resp_href.encoding = "utf-8"

    href_page = BeautifulSoup(resp_href.text, "html.parser")
    aherf = href_page.find("p",align="center")
    img = aherf.find("img")
    src = img.get("src")
    #下载图片
    img_resp = requests.get(src)
    img_resp.content #拿到图片字节
    img_name = src.split("/")[-1]#拿到url的最后一个/以后的内容
    with open("img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)
    time.sleep(1)
    print("over",img_name)
print("over")
resp.close()
resp_href.close()














