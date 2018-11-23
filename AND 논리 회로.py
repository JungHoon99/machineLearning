'''
1. AND 논리 회로 구현

2. 가중치와 편향 도입
'''

#1
x=[[0,0],[0,1],[1,1],[1,0]]

def AND(x,y):
    w1,w2,theta=0.5,0.5,0.8
    tmp=(x*w1)+(y*w2)
    if(tmp<=theta):
        return 0
    elif(tmp>theta):
        return 1

print("AND 논리 회로")
for i in range(4):
    pt=AND(x[i][0],x[i][1])
    print(pt)


#2
import numpy as np

x=0
y=1

def AND2(x,y):
    h=np.array([x,y])
    w=np.array([0.5,0.5])
    b=-0.7

    tmp=np.sum(h*w)+b
    if(tmp<=0):
        return 0
    elif(tmp>0):
        return 1

#ㄴㅁㅇㄴㅁㅇㅁㅇㅁ
print(AND(x,y))
