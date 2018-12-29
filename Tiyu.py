#coding=utf-8
from random import random

def printbt():
    print('a与b比赛')
    print('输入a与b的能力值(0-1)')

def getinput():
    a=eval(input('a的能力值:'))
    b=eval(input('b的能力值:'))
    n=eval(input('比赛场次:'))
    return a,b,n

def printjg(wina,winb):
    n=wina+winb
    print('共模拟{}场比赛'.format(n))
    print('a赢{}场比赛,占比{:0.1%}'.format(wina,wina/n))
    print('b赢{}场比赛,占比{:0.1%}'.format(winb,winb/n))

def gameover(a,b):
    return a==15 or b==15

def simonegame(proba,probb):
    scorea,scoreb=0,0
    serving='a'
    while not gameover(scorea,scoreb):
        if serving=='a':
            if random()<proba:
                scorea+=1
            else:
                serving='b'
        else:
            if random()<probb:
                scoreb+=1
            else:
                serving='a'
    return scorea,scoreb

def simngames(n,proba,probb):
    winsa,winsb=0,0
    for i in range(n):
        scorea,scoreb=simonegame(proba,probb)
        if scorea>scoreb:
            winsa+=1
        else:
            winsb+=1
    return winsa,winsb

def main():
    printbt()
    proba,probb,n=getinput()
    winsa,winsb=simngames(n,proba,probb)
    printjg(winsa,winsb)

main()