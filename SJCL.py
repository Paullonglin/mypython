#一组数据处理
def getnum():
    nums=[]
    inumstr=input('请输入数字(回车退出):')
    while inumstr !='':
        nums.append(eval(inumstr))
        inumstr=input('请输入数字(回车退出):')
    return nums

def ver(numbers):
    s=0.0
    for i in numbers:
        s=s+i
    return s/len(numbers)

def fc(numbers,ver):
    sfc=0.0
    for i in numbers:
        sfc=sfc+(i-ver)**2
    return pow(sfc/(len(numbers)-1),0.5)

def med(numbers):
    sorted(numbers)
    smed=0.0
    if len(numbers)%2==0:
        smed=(numbers[len(numbers)//2-1]+numbers[len(numbers)//2])/2
    else:
        smed=(numbers[len(numbers)//2])
    return smed

n=getnum()
v=ver(n)
print('平均值:,{}方差:{:.2},中位数:{}'.format(v,fc(n,v),med(n)))
