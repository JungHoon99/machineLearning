'''
1. 배운것을 토대로 NAND와 OR 게이트 구하기

2. 다중 퍼셉트론을 이용한 XOR게이트
'''
import numpy as np

x=0
y=0

def NAND(x,y):
    h=np.array([x,y])
    w=np.array([-0.5,-0.5])
    b=0.7

    tmp=np.sum(h*w)+b
    if( tmp<=0 ):
        return 0
    elif(tmp>0):
        return 1

def OR(x,y):
    h=np.array([x,y])
    w=np.array([0.5,0.5])
    b=-0.2

    tmp=np.sum(h*w)+b
    if(tmp<=0):
        return 0
    elif(tmp>0):
        return 1

print("NAND:",NAND(x,y))
print("OR:",OR(x,y))

def AND(x,y):
    h=np.array([x,y])
    w=np.array([0.5,0.5])
    b=-0.7

    tmp=np.sum(h*w)+b

    if(tmp>0):
        return 1
    elif(tmp<=0):
        return 0

#XOR게이트

print(AND(NAND(x,y),OR(x,y)))

    
