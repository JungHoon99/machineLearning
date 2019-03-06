#5문항에 대해 대답을 하지만 18개의 학습집합으로도 학습이 아주 잘됨 
from urllib.request import urlopen, Request
import urllib
import bs4

def craw(weather):
    location = str(weather)
    enc_location = urllib.parse.quote(location + '+날씨')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    return bs4.BeautifulSoup(html,'html5lib')

soup = craw("")

#날씨 웹크롤링 객체화
class weather():
    def __init__(self):
        self.degree=0
        self.high_d=0
        self.low_d=0
        self.cast=0
        self.dust=0
        self.tomorrow=0
        self.next_tomorrow=0
        
    def crawling(self):
        self.degree=soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text
        self.high_d=soup.find('ul', class_='info_list').find('span', class_='max').find('span', class_='num').text
        self.low_d=soup.find('ul', class_='info_list').find('span', class_='min').find('span', class_='num').text
        self.cast=soup.find('ul', class_='info_list').find('p', class_='cast_txt').text
        self.dust=(str(soup.find('dl', class_='indicator').text).split()[1][:len(str(soup.find('dl', class_='indicator').text).split()[1])-2],str(soup.find('dl', class_='indicator').text).split()[1][-2:])
        self.tomorrow=(soup.find('div', class_='tomorrow_area').text.split()[:soup.find('div', class_='tomorrow_area').text.split().index("미세먼지")+2],soup.find('div', class_='tomorrow_area').text.split()[soup.find('div', class_='tomorrow_area').text.split().index("미세먼지")+2:soup.find('div', class_='tomorrow_area').text.split().index("미세먼지")+2+soup.find('div', class_='tomorrow_area').text.split()[soup.find('div', class_='tomorrow_area').text.split().index("미세먼지")+2:].index("미세먼지")+2])
        self.next_tomorrow=(soup.find('div',class_='tomorrow_area day_after _mainTabContent').text.split()[:soup.find('div', class_='tomorrow_area day_after _mainTabContent').text.split().index("미세먼지")+2],soup.find('div', class_='tomorrow_area day_after _mainTabContent').text.split()[soup.find('div', class_='tomorrow_area day_after _mainTabContent').text.split().index("미세먼지")+2:soup.find('div', class_='tomorrow_area day_after _mainTabContent').text.split().index("미세먼지")+2+soup.find('div', class_='tomorrow_area day_after _mainTabContent').text.split()[soup.find('div', class_='tomorrow_area day_after _mainTabContent').text.split().index("미세먼지")+2:].index("미세먼지")+2])

    def get_degree(self):   #현재 온도 반환
        return self.degree

    def get_high_d(self):   #오늘의 최고기온
        return self.high_d

    def get_low_d(self):    #오늘의 최저기온
        return self.low_d

    def get_cast(self):     #현재 날씨 상황
        return self.cast

    def get_dust(self):     #미세먼지 지수
        return self.dust

    def get_tomorrow(self):
        return self.tomorrow

    def get_next_tomorrow(self):
        return self.next_tomorrow

# one_hot 벡터화 함수
def vectorize_sequences(sequences,diemension=33182):
    result=np.zeros((len(sequences),diemension))
    for i,sequence in enumerate(sequences):
        result[i,sequence]=1.
    return result

#파일 읽어오기
with open('words2.txt','rt') as f:
    text=f.read()
with open('words.txt','rt') as l:
    location=l.read()

#뛰어쓰기 대로 파싱
text=text.split()

#형태소 분석
for i in range(len(text)):
    senten.extend(k.pos(text[i]))

#단어 분리
for i in range(len(senten)):
    if((senten[i][0] in sentence)==False):
        sentence.append(senten[i][0])

del senten
a=0
for i in range(len(sentence)):
    if(dic.get(sentence[i])==check):
        dic.update({sentence[i]:a})
        a+=1

del sentence

#학습 문장 데이터
senten=["오늘은 날씨는 어때","오늘 날씨 좀 알려줘",
"오늘 날씨 어때","오늘 날씨 좋아","오늘은 날씨가 어때",
"안녕","안녕하세요","오늘 최고기온이 몇도야",
"오늘 최고기온","최고기온은","최고기온","오늘 최저기온이 몇도야",
"오늘 최저기온","최저기온은","최저기온","미세먼지 어때?","미세먼지 알려줘",
"미세먼지 안좋아?","오늘 어때","오늘 좋을까 안좋을까?","오늘 안좋아?"]

x_train=[]
# 학습 문장에 맞는 결과 데이터
y_train=[[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],
         [0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0],
         [0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0]]


#학습 문장 과 결과 데이터 가공
for j in range(len(senten)):
    test=k.pos(senten[j])
    data=[]
    for i in range(len(test)):
        data.extend([dic.get( test[i][0])])
    x_train.append(list(data))

x_train=vectorize_sequences(x_train)

y_train=np.array(y_train)

#딥러닝 학습 모듈
from keras import models
from keras import layers
from keras import optimizers

#모델 설정
model = models.Sequential()
#총 3개의 은닉층을 가진 모델 층 쌓기  
model.add(layers.Dense(16,activation='relu',input_shape=(33182,)))
model.add(layers.Dense(16,activation='softmax'))
model.add(layers.Dense(9,activation='softmax'))

#모델의 옵티마이저 설정과 손실 함수 설정
model.compile(optimizer=optimizers.RMSprop(lr=0.001),loss='categorical_crossentropy',metrics=['acc'])

#모델 학습
model.fit(x_train,y_train,batch_size=21 ,epochs=3000)

W=weather()
W.crawling()

#학습 신경망에서의 결과 출력
def request():
    global soup
    senten=k.pos(ent.get())
    x_test=[]
    data=[]
    day=0
    for i in range(len(senten)):
        if((senten[i][0] in location.split()) == True):
            soup=craw(senten[i][0])
            del senten[i]
            break
        
    for i in range(len(senten)):
        if((senten[i][0] in '오늘')== True):
            day=0
        elif((senten[i][0] in '내일')== True):
            day=1
        elif((senten[i][0] in '모레')== True):
            day=2
        
    for i in range(len(senten)):
        data.extend([dic.get( senten[i][0])])
        
    x_test.append(list(data))
    
    for i in range(x_test[0].count(None)):
        x_test[0].remove(None)
        
    x_test=vectorize_sequences(x_test)
    predict = model.predict(x_test).argmax(axis=1)
    action(predict,day)

#대답
def action(kind,day):
    W=weather()
    W.crawling()
    if(kind==0 and day==0):
        lab['text']="날씨는 "+str(W.get_cast())+" (현재온도 : "+ str(W.get_degree())+")"
    elif(kind==1 and day==0):
        lab['text']="안녕하세요"
    elif(kind==2 and day==0):
        lab['text']="최고기온은 "+str(W.get_high_d())+"도씨℃ 입니다."
    elif(kind==3 and day==0):
        lab['text']="최저기온은 "+str(W.get_low_d())+"도씨℃ 입니다."
    elif(kind==4 and day==0):
        a=W.get_dust()
        lab['text']="미세먼지는 "+a[0]+"로 "+a[1]+"이에요"
        
    elif(kind==0 and day==1):
        lab['text']=" 내일 날씨는 "+str(W.get_tomorrow()[0][2:-2])[1:-1]+"이에요"+" (현재온도 : "+ str(W.get_degree())+")"
    elif(kind==1 and day==1):
        lab['text']="안녕하세요"
    elif(kind==2 and day==1):
        lab['text']="내일 최고기온은 "+str(W.get_tomorrow()[1][1])+" 입니다."
    elif(kind==3 and day==1):
        lab['text']="내일 최저기온은 "+str(W.get_tomorrow()[0][1])+" 입니다."
    elif(kind==4 and day==1):
        lab['text']="미세먼지는 "+str(W.get_tomorrow()[0][-1])+"이에요"

    elif(kind==0 and day==2):
        lab['text']="모레 날씨는 "+str(W.get_next_tomorrow()[0][2:-2])[1:-1]+"이에요"+" (현재온도 : "+ str(W.get_degree())+")"
    elif(kind==1 and day==2):
        lab['text']="안녕하세요"
    elif(kind==2 and day==2):
        lab['text']="모레 최고기온은 "+str(W.get_next_tomorrow()[1][1])+" 입니다."
    elif(kind==3 and day==2):
        lab['text']="모레 최저기온은 "+str(W.get_next_tomorrow()[0][1])+" 입니다."
    elif(kind==4 and day==2):
        lab['text']="미세먼지는 "+str(W.get_next_tomorrow()[0][-1])+"이에요"

from tkinter import *

main=Tk()

ent=Entry(main,width=70)
ent.grid()
but=Button(main,text='확인',command=request)
but.grid(row=0,column=1)
lab=Label(main,text='대답')
lab.grid(row=1,column=0)

mainloop()
