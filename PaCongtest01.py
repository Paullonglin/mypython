import requests
r=requests.get('https://www.baidu.com')
if r.status_code==200:
    r.encoding=r.apparent_encoding
    fo=open('pc.txt','w+')
    ls=r.text
    fo.writelines(ls)
    fo.seek(0)
    for line in fo:
        print(line)
    fo.close()
