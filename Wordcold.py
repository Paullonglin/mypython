#词云
import jieba
import wordcloud
from scipy.misc import imread
import matplotlib
mask=imread('abc.jpg')
f=open('1.txt','rt',encoding="GBK")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)

w=wordcloud.WordCloud(font_path='msyh.ttc',max_words=20,mask=mask,width=1000,height=700,background_color='white')
w.generate(txt)
w.to_file('1.png')



