from urllib.request import urlopen
url = "http://www.baidu.com"
#获取响应
resp = urlopen(url)

with open('mybaidu.html', mode='w', encoding='utf-8') as f:
     f.write(resp.read().decode('utf-8'))
#存储
print('over!')
