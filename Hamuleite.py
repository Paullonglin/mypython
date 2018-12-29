#hamlet 单词统计
def getwords():
    words=open('Hamlet.txt','r').read()
    words=words.lower()
    for ch in '!@#$%^&*()_+-=<>?:",./[]{}\|':
        words=words.replace(ch,' ')
    return words

hamlettxt=getwords()
txt=hamlettxt.split()
count={}
for word in txt:
    count[word]=count.get(word,0)+1
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{:<10}{:>5}'.format(word,count))
