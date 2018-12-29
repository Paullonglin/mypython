#coding=utf-8
import requests
import os
url='http://www.pearvideo.com/video_1466021'
root='F://shucai//'
path=root+url.split('/')[-1]
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url,headers=kv)
        print(r.text)
    else:
        print('文件已存在')
except:
    print('爬取失败')
