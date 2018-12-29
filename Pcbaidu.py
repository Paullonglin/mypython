#coding=utf-8
import requests
key='假面骑士'
try:
    kv={'wd':key}
    r=requests.get('https://www.baidu.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')