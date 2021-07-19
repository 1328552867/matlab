import requests

url ='https://fanyi.baidu.com/sug'
s = input('请输入你要翻译的单词')
dat ={
    'kw':s
}

resp = requests.post(url,data=dat)
#地址栏上的提交统一是get方式
print(resp.json())#将服务器里返回的内容直接转换为json
