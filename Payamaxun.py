import requests
url='https://www.amazon.cn/dp/B01ION3VWI/ref=sr_1_1?s=books&srs=658414051&ie=UTF8&qid=1541411554&sr=1-1'
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print('filure')
