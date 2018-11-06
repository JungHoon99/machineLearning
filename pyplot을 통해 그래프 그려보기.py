'''
matplotlib안에 있는pyplot모듈을 사용해 그래프를 그려보기
'''
import numpy as np
import matplotlib.pyplot as pl

x=np.arange(0,6.1,0.1) #0부터 6까지 0.1 간격으로 np리스트에 저장
y=np.sin(x)

print(x)

pl.plot(x,y)
pl.show()
