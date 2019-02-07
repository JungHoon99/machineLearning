from konlpy.tag import Twitter
import numpy as np

check=None
k=Twitter()
senten=[]
sentence=[]
dic={}

#데이터 학습을 위 한 전처리 함수
def vectorize_sequences(sequences,diemension=33154):
    result=np.zeros((len(sequences),diemension))
    for i,sequence in enumerate(sequences):
        result[i,sequence]=1.
    return result

#파일 불러오기
with open('words2.txt','rt') as f:
    text=f.read()

#파싱 하기
text=text.split()

#형태소 분석
for i in range(len(text)):
    senten.extend(k.pos(text[i]))

for i in range(len(senten)):
    if((senten[i][0] in sentence)==False):
        sentence.append(senten[i][0])

del senten
a=0
for i in range(len(sentence)):
    if(dic.get(sentence[i])==check):
        dic.update({sentence[i]:a})
        a+=1

#훈련에 사용 되는 문장들 형재 날씨와 최고기온 최저기온 미세먼지상태를 질문 가능하게 함
senten=["오늘은 날씨는 어때","오늘 날씨 좀 알려줘",
"오늘 날씨 어때","오늘 날씨 좋아","오늘은 날씨가 어때",
"안녕","안녕하세요","오늘 최고기온이 몇도야",
"오늘 최고기온","최고기온은","최고기온","오늘 최저기온이 몇도야",
"오늘 최저기온","최저기온은","최저기온","미세먼지 어때?","미세먼지 알려줘","미세먼지 안좋아?"]

x_train=[]
#매칭되는 결과값들 one-hot 으로 표현
y_train=[[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],
         [0,1,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],
         [0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]


for j in range(len(senten)):
    test=k.pos(senten[j])
    data=[]
    for i in range(len(test)):
        data.extend([dic.get( test[i][0])])
    x_train.append(list(data))

x_train=vectorize_sequences(x_train)

y_train=np.array(y_train)

from keras import models
from keras import layers
from keras import optimizers

model = models.Sequential()
model.add(layers.Dense(16,activation='relu',input_shape=(33154,)))
model.add(layers.Dense(16,activation='softmax'))
model.add(layers.Dense(5,activation='softmax'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001),loss='categorical_crossentropy',metrics=['acc'])

model.fit(x_train,y_train,batch_size=18 ,epochs=2500)

def request():
    senten=k.pos(ent.get())
    x_test=[]
    data=[]
    for i in range(len(senten)):
        data.extend([dic.get( senten[i][0])])
    x_test.append(list(data))
    if(len(x_test)==0):
        lab['text']="제가 할 수 없는 일이에요"
    x_test=vectorize_sequences(x_test)
    predict = model.predict(x_test).argmax(axis=1)
    lab['text']=predict

from tkinter import *

main=Tk()

ent=Entry(main,width=100)
ent.grid()
but=Button(main,text='확인',command=request)
but.grid(row=0,column=1)
lab=Label(main,text='대답')
lab.grid(row=1,column=0)

mainloop()
