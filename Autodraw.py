#自动轨迹绘制
import turtle as t
t.title('自动绘制轨迹')
t.setup(800,600,0,0)
t.pensize(5)
t.pencolor('red')
#数据读取
lsnew=[]
f=open('data.txt','rt')
for line in f:
    line=line.replace('\n',' ')
    lsnew.append(list(map(eval,line.split(','))))
f.close()
#绘制图形
for i in range(len(lsnew)):
    t.pencolor(lsnew[i][3],lsnew[i][4],lsnew[i][5])
    t.fd(lsnew[i][0])
    if lsnew[i][1]:
        t.right(lsnew[i][2])
    else:
        t.left(lsnew[i][2])
