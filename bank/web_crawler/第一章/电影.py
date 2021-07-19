import requests
headers ={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url ='https://movie.douban.com/j/chart/top_list'
#重新封装参数
param ={
    'type': '24',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'20'
    }

resp = requests.get(url=url,params=param,headers=headers)
#地址栏上的提交统一是get方式
print(resp.json())#将服务器里返回的内容直接转换为json
resp.close()#关闭resp

