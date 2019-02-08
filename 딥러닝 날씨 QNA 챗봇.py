#5문항에 대해 대답을 하지만 18개의 학습집합으로도 학습이 아주 잘됨 
from konlpy.tag import Twitter
import numpy as np

check=None
k=Twitter()
senten=[]
sentence=[]
dic={}


#웹 크롤링 객체
from urllib.request import urlopen, Request
import urllib
import bs4
import time

location = ''
enc_location = urllib.parse.quote(location + '+날씨')

url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
type(html)
soup = bs4.BeautifulSoup(html,'html5lib')

class weather():
    def __init__(self):
        self.today=0
        self.degree=0
        self.high_d=0
        self.low_d=0
        self.cast=0
        self.dust=0
        
    def crawling(self):
        self.degree=soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
        self.high_d=soup.find('ul', class_='info_list').find('span', class_='max').find('span', class_='num').text
        self.low_d=soup.find('ul', class_='info_list').find('span', class_='min').find('span', class_='num').text
        self.cast=soup.find('ul', class_='info_list').find('p', class_='cast_txt').text

    def get_degree(self):
        return self.degree

    def get_high_d(self):
        return self.high_d

    def get_low_d(self):
        return self.low_d

    def get_cast(self):
        return self.cast

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
    x_test=vectorize_sequences(x_test)
    predict = model.predict(x_test).argmax(axis=1)
    lab['text']=predict
    
def action(kind):
    W=weather()
    W.crawling()
    if(kind==0):
        lab['text']=str(W.get_cast())
    elif(kind==1):
        lab['text']="안녕하세요"
    elif(kind==2):
        lab['text']=str(W.get_high_d())
    elif(kind==3):
        lab['text']=str(W.get_low_d())
    elif(kind==4):
        lab['text']="미세먼지는 안좋아요"

from tkinter import *

main=Tk()

ent=Entry(main,width=100)
ent.grid()
but=Button(main,text='확인',command=request)
but.grid(row=0,column=1)
lab=Label(main,text='대답')
lab.grid(row=1,column=0)

mainloop()
