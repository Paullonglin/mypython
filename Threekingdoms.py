#三国演义
import jieba
txt=open('threekingdoms.txt','r',encoding="utf-8").read()
excludes={'将军','却说'}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=='诸葛亮' or word=='孔明曰':
        rword='孔明'
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{:<10}{:>5}'.format(word,count))
