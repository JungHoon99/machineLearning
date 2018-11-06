import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10,0.1) #0부터 10까지의 0.1만큼 간격으로 리스트에 저장

y=np.sin(x) #x에 대조되는 sin값을 리스트에 저장
z=np.cos(x) #x에 대조되는 cos값을 리스트에 저장

print(y)
print(z)

plt.plot(x,y,label="sin")  #그래프를 그리고 이름을 sin이라고 지정
plt.plot(x,z,linestyle="--",label="cos") #그래프를 그리고 이름을 cos이라고 지정 라인 표스 스타일은 -- 이것이다.
plt.xlabel("x")  #x축에 이름은 x
plt.ylabel("y")  #y축에 이름은 y
plt.title("sin & cos") #그래프 이름 표시
plt.legend()     #그래프 안에 x가 무슨 선이고 y가 무슨 선인지 표
plt.show()       #plt화면을 보여줘
