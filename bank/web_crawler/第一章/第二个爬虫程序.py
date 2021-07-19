import requests

query=input('请输入你想搜索的内容')
url =f'https://www.sogou.com/web?query={query}'
#用户标识
headers ={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

resp = requests.get(url,headers=headers)
#地址栏上的提交统一是get方式

print(resp)
print(resp.text)


