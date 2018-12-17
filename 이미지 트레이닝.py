#이미지 하나가 오버플로우 되는 형상이 있다.
from keras import datasets
import numpy as np
import pickle
import time

mid=[]
(x_train,t_train),(x_test,t_test)=datasets.mnist.load_data()

with open ("sample_weight.pkl","rb") as f:
    network=pickle.load(f)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def foward(network,x):
    w1,w2,w3=network['W1'],network['W2'],network['W3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']
    for i in range(28):
        for j in range(28):
            mid.append(x[i][j])
    t=tuple(mid)
    a1=np.dot(t,w1)+b1
    z1=sigmoid(a1)
    a2=np.dot(z1,w2)+b2
    z2=sigmoid(a2)
    a3=np.dot(z2,w3)+b3
    y=a3
    mid.clear()
    return y

accuracy_cnt=0

for i in range(len(x_test)):
    y = foward(network,x_test[i])
    p=np.argmax(y)
    if(p == t_test[i]):
        accuracy_cnt+=1

print(float(accuracy_cnt)/len(x_test))


''' 트레이닝 첫번째 이미지 보여주기
def show(img):
    pil=Image.fromarray(np.uint8(img))
    pil.show()
    
img_x=x_train[0]
print(img_x.shape)
show(img_x)
'''
