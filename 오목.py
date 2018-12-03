from tkinter import*
import random
import time

main=Tk()

pos=[]
infor=[]

for i in range(20):
    infor.append([])
    for j in range(20):
        pos.append([20*j,20*i])
        infor[i].append(0)

#오목 게임 객체화
class Omok:
    def __init__(self,can,pos,x):
        self.can=can
        self.pos=pos
        self.color=["black","white"]
        self.x=x
        self.count=0;

    def make_line(self):
        for i in range(20):
            self.can.create_line(20*i,0,20*i,380)
        for i in range(20):
            self.can.create_line(0,20*i,380,20*i)

    def draw(self,event):
        for i in range(20):
            for j in range(20):
                if(event.x>self.pos[j+(i*20)][0]-10 and event.x<(self.pos[j+(i*20)][0]+10)):
                    if(event.y>self.pos[j+(i*20)][1]-10 and event.y<self.pos[j+(i*20)][1]+10):
                        if(infor[i][j]==0):
                            self.can.create_oval(self.pos[j+(i*20)][0]-9,self.pos[j+(i*20)][1]-9,self.pos[j+(i*20)][0]+9,self.pos[j+(i*20)][1]+9,fill="white")
                            infor[i][j]=1
                            computer()
                            Match()

    def check(self,event):
        for i in range(20):
            for j in range(20):
                if(event.x>self.pos[j+(i*20)][0]-10 and event.x<(self.pos[j+(i*20)][0]+10)):
                    if(event.y>self.pos[j+(i*20)][1]-10 and event.y<self.pos[j+(i*20)][1]+10):
                        self.can.create_oval(self.pos[j+(i*20)][0]-9,self.pos[j+(i*20)][1]-9,self.pos[j+(i*20)][0]+9,self.pos[j+(i*20)][1]+9,tags="ch")

    def delete(self,event):
        self.can.delete("ch")
                    
#승부 판단 함수
def Match():
    for i in range(20):
        for j in range(16):
            low=0
            column=0
            for k in range(5):
                if(infor[i][j+k]==1):
                    low+=1
                elif(infor[j+k][i]==1):
                    column+=1
            if(low==5 or column==5):
                end=Tk()
                lbl=Label(end,text="흰색돌이이겼습니다")
                lbl.pack()
                return 0

    for i in range(16):
        for j in range(16-i):
            top=0
            bottom=0
            for k in range(5):
                if(infor[k+j][k+j+i]==1):
                    top+=1
                elif(infor[k+j+i][k+j]==1):
                    bottom+=1
            if(top==5 or bottom==5):
                end=Tk()
                lbl=Label(end,text="흰색돌이이겼습니다")
                lbl.pack()
                return 0
            
            top=0
            bottom=0
            for k in range(5):
                if(infor[k+j][19-(k+j+i)]==1):
                    top+=1
                elif(infor[k+j+i][19-(k+j)]==1):
                    bottom+=1
            if(top==5 or bottom==5):
                end=Tk()
                lbl=Label(end,text="흰색돌이이겼습니다")
                lbl.pack()
                return 0

    for i in range(20):
        for j in range(16):
            low=0
            column=0
            for k in range(5):
                if(infor[i][j+k]==10):
                    low+=1
                elif(infor[j+k][i]==10):
                    column+=1
            if(low==5 or column==5):
                end=Tk()
                lbl=Label(end,text="검은색돌이 이겼습니다")
                lbl.pack()
                return 0

    for i in range(16):
        for j in range(16-i):
            top=0
            bottom=0
            for k in range(5):
                if(infor[k+j][k+j+i]==10):
                    top+=1
                elif(infor[k+j+i][k+j]==10):
                    bottom+=1
            if(top==5 or bottom==5):
                end=Tk()
                lbl=Label(end,text="검은색돌이 이겼습니다")
                lbl.pack()
                return 0
            top=0
            bottom=0
            for k in range(5):
                if(infor[k+j][19-(k+j+i)]==10):
                    top+=1
                elif(infor[k+j+i][19-(k+j)]==10):
                    bottom+=1
            if(top==5 or bottom==5):
                end=Tk()
                lbl=Label(end,text="검은색돌이 이겼습니다")
                lbl.pack()
                return 0




#컴퓨터
include=0
def computer():
    global include
    if(include==0):
        canvas.create_oval(pos[10+(10*20)][0]-9,pos[10+(10*20)][1]-9,pos[10+(10*20)][0]+9,pos[10+(10*20)][1]+9,fill="black")
        infor[10][10]=10
        include+=1
    else:
        #대각선 4개 검사 공격
        for i in range(16):
            for j in range(16-i):
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][k+j+i]==10):
                        top+=1
                    elif(infor[k+j+i][k+j]==10):
                        bottom+=1
                if(top==4):
                    for k in range(5):
                        if(infor[k+j][k+j+i]==0):
                            canvas.create_oval(pos[(k+j+i)+((k+j)*20)][0]-9,pos[(k+j+i)+((k+j)*20)][1]-9,pos[(k+j+i)+((k+j)*20)][0]+9,pos[(k+j+i)+((k+j)*20)][1]+9,fill="black")
                            infor[k+j][k+j+i]=10
                            return 0
                elif(bottom==4):
                    for k in range(5):
                        if(infor[k+j+i][k+j]==0):
                            canvas.create_oval(pos[(k+j)+((k+j+i)*20)][0]-9,pos[(k+j)+((k+j+i)*20)][1]-9,pos[(k+j)+((k+j+i)*20)][0]+9,pos[(k+j)+((k+j+i)*20)][1]+9,fill="black")
                            infor[k+j+i][k+j]=10
                            return 0
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][19-(k+j+i)]==10):
                        top+=1
                    elif(infor[k+j+i][19-(k+j)]==10):
                        bottom+=1
                if(top==4):
                    for k in range(5):
                        if(infor[k+j][19-(k+j+i)]==0):
                           canvas.create_oval(pos[(19-(k+j+i))+((k+j)*20)][0]-9,pos[(19-(k+j+i))+((k+j)*20)][1]-9,pos[(19-(k+j+i))+((k+j)*20)][0]+9,pos[(19-(k+j+i))+((k+j)*20)][1]+9,fill="black")
                           infor[k+j][19-(k+j+i)]=10
                           return 0
                elif(bottom==4):
                    for k in range(5):
                        if(infor[k+j+i][19-(k+j)]==0):
                           canvas.create_oval(pos[(19-(k+j))+((k+j+i)*20)][0]-9,pos[(19-(k+j))+((k+j+i)*20)][1]-9,pos[(19-(k+j))+((k+j+i)*20)][0]+9,pos[(19-(k+j))+((k+j+i)*20)][1]+9,fill="black")
                           infor[k+j+i][19-(k+j)]=10
                           return 0

        #가로 세로 4개 검사 공격
        for i in range(20):
            for j in range(16):
                low=0
                column=0
                for k in range(5):
                    if(infor[i][j+k]==10):
                        low+=1
                    elif(infor[j+k][i]==10):
                        column+=1
                if(low==4):
                    for k in range(5):
                        if(infor[i][j+k]==0):
                            canvas.create_oval(pos[(k+j)+(i*20)][0]-9,pos[(k+j)+(i*20)][1]-9,pos[(k+j)+(i*20)][0]+9,pos[(k+j)+(i*20)][1]+9,fill="black")
                            infor[i][j+k]=10
                            return 0
                elif(column==4):
                    for k in range(5):
                        if(infor[j+k][i]==0):
                            canvas.create_oval(pos[i+((k+j)*20)][0]-9,pos[i+((k+j)*20)][1]-9,pos[i+((k+j)*20)][0]+9,pos[i+((k+j)*20)][1]+9,fill="black")
                            infor[j+k][i]=10
                            return 0
                        
        #대각선 4개 검사 방어
        for i in range(16):
            for j in range(16-i):
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][k+j+i]==1):
                        top+=1
                    elif(infor[k+j+i][k+j]==1):
                        bottom+=1
                if(top==4):
                    for k in range(5):
                        if(infor[k+j][k+j+i]==0):
                            canvas.create_oval(pos[(k+j+i)+((k+j)*20)][0]-9,pos[(k+j+i)+((k+j)*20)][1]-9,pos[(k+j+i)+((k+j)*20)][0]+9,pos[(k+j+i)+((k+j)*20)][1]+9,fill="black")
                            infor[k+j][k+j+i]=10
                            return 0
                elif(bottom==4):
                    for k in range(5):
                        if(infor[k+j+i][k+j]==0):
                            canvas.create_oval(pos[(k+j)+((k+j+i)*20)][0]-9,pos[(k+j)+((k+j+i)*20)][1]-9,pos[(k+j)+((k+j+i)*20)][0]+9,pos[(k+j)+((k+j+i)*20)][1]+9,fill="black")
                            infor[k+j+i][k+j]=10
                            return 0
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][19-(k+j+i)]==1):
                        top+=1
                    elif(infor[k+j+i][19-(k+j)]==1):
                        bottom+=1
                if(top==4):
                    for k in range(5):
                        if(infor[k+j][19-(k+j+i)]==0):
                           canvas.create_oval(pos[(19-(k+j+i))+((k+j)*20)][0]-9,pos[(19-(k+j+i))+((k+j)*20)][1]-9,pos[(19-(k+j+i))+((k+j)*20)][0]+9,pos[(19-(k+j+i))+((k+j)*20)][1]+9,fill="black")
                           infor[k+j][19-(k+j+i)]=10
                           return 0
                elif(bottom==4):
                    for k in range(5):
                        if(infor[k+j+i][19-(k+j)]==0):
                           canvas.create_oval(pos[(19-(k+j))+((k+j+i)*20)][0]-9,pos[(19-(k+j))+((k+j+i)*20)][1]-9,pos[(19-(k+j))+((k+j+i)*20)][0]+9,pos[(19-(k+j))+((k+j+i)*20)][1]+9,fill="black")
                           infor[k+j+i][19-(k+j)]=10
                           return 0

        #가로세로 4개 검사 방어
        for i in range(20):
            for j in range(16):
                low=0
                column=0
                for k in range(5):
                    if(infor[i][j+k]==1):
                        low+=1
                    elif(infor[j+k][i]==1):
                        column+=1
                if(low==4):
                    for k in range(5):
                        if(infor[i][j+k]==0):
                            canvas.create_oval(pos[(k+j)+(i*20)][0]-9,pos[(k+j)+(i*20)][1]-9,pos[(k+j)+(i*20)][0]+9,pos[(k+j)+(i*20)][1]+9,fill="black")
                            infor[i][j+k]=10
                            return 0
                elif(column==4):
                    for k in range(5):
                        if(infor[j+k][i]==0):
                            canvas.create_oval(pos[i+((k+j)*20)][0]-9,pos[i+((k+j)*20)][1]-9,pos[i+((k+j)*20)][0]+9,pos[i+((k+j)*20)][1]+9,fill="black")
                            infor[j+k][i]=10
                            return 0

        #대각선 3개 검사 공격
        for i in range(16):
            for j in range(16-i):
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][k+j+i]==10):
                        top+=1
                    elif(infor[k+j+i][k+j]==10):
                        bottom+=1
                if(top==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][k+j+i]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j][k+j+i]==0):
                                canvas.create_oval(pos[(k+j+i)+((k+j)*20)][0]-9,pos[(k+j+i)+((k+j)*20)][1]-9,pos[(k+j+i)+((k+j)*20)][0]+9,pos[(k+j+i)+((k+j)*20)][1]+9,fill="black")
                                infor[k+j][k+j+i]=10
                                return 0
                elif(bottom==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][k+j+i]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j+i][k+j]==0):
                                canvas.create_oval(pos[(k+j)+((k+j+i)*20)][0]-9,pos[(k+j)+((k+j+i)*20)][1]-9,pos[(k+j)+((k+j+i)*20)][0]+9,pos[(k+j)+((k+j+i)*20)][1]+9,fill="black")
                                infor[k+j+i][k+j]=10
                                return 0
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][19-(k+j+i)]==10):
                        top+=1
                    elif(infor[k+j+i][19-(k+j)]==10):
                        bottom+=1
                if(top==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][19-(k+j+i)]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j][19-(k+j+i)]==0):
                               canvas.create_oval(pos[(19-(k+j+i))+((k+j)*20)][0]-9,pos[(19-(k+j+i))+((k+j)*20)][1]-9,pos[(19-(k+j+i))+((k+j)*20)][0]+9,pos[(19-(k+j+i))+((k+j)*20)][1]+9,fill="black")
                               infor[k+j][19-(k+j+i)]=10
                               return 0
                elif(bottom==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j+i][17-k+j]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j+i][17-(k+j)]==0):
                               canvas.create_oval(pos[(17-(k+j))+((k+j+i)*20)][0]-9,pos[(17-(k+j))+((k+j+i)*20)][1]-9,pos[(17-(k+j))+((k+j+i)*20)][0]+9,pos[(17-(k+j))+((k+j+i)*20)][1]+9,fill="black")
                               infor[k+j+i][17-(k+j)]=10
                               return 0
                        
        #가로 세로 3개 검사 공격
        for i in range(20):
            for j in range(16):
                low=0
                column=0
                for k in range(5):
                    if(infor[i][j+k]==10):
                        low+=1
                    elif(infor[j+k][i]==10):
                        column+=1
                if(low==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[i][j+k]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[i][j+k]==0):
                                canvas.create_oval(pos[(k+j)+((i)*20)][0]-9,pos[(k+j)+((i)*20)][1]-9,pos[(k+j)+((i)*20)][0]+9,pos[(k+j)+((i)*20)][1]+9,fill="black")
                                infor[i][j+k]=10
                                return 0
                elif(column==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[j+k][i]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[j+k][i]==0):
                                canvas.create_oval(pos[(i)+((k+j)*20)][0]-9,pos[(i)+((k+j)*20)][1]-9,pos[(i)+((k+j)*20)][0]+9,pos[i+((k+j)*20)][1]+9,fill="black")
                                infor[j+k][i]=10
                                return 0

        #대각선 3개 검사 방어
        for i in range(16):
            for j in range(16-i):
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][k+j+i]==1):
                        top+=1
                    elif(infor[k+j+i][k+j]==1):
                        bottom+=1
                if(top==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][k+j+i]==10):
                                continue
                        apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j][k+j+i]==0):
                                canvas.create_oval(pos[(k+j+i)+((k+j)*20)][0]-9,pos[(k+j+i)+((k+j)*20)][1]-9,pos[(k+j+i)+((k+j)*20)][0]+9,pos[(k+j+i)+((k+j)*20)][1]+9,fill="black")
                                infor[k+j][k+j+i]=10
                                return 0
                elif(bottom==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][k+j+i]==10):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j+i][k+j]==0):
                                canvas.create_oval(pos[(k+j)+((k+j+i)*20)][0]-9,pos[(k+j)+((k+j+i)*20)][1]-9,pos[(k+j)+((k+j+i)*20)][0]+9,pos[(k+j)+((k+j+i)*20)][1]+9,fill="black")
                                infor[k+j+i][k+j]=10
                                return 0

                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][19-(k+j+i)]==1):
                        top+=1
                    elif(infor[k+j+i][19-(k+j)]==1):
                        bottom+=1
                if(top==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][19-(k+j+i)]==10):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j][19-(k+j+i)]==0):
                               canvas.create_oval(pos[(19-(k+j+i))+((k+j)*20)][0]-9,pos[(19-(k+j+i))+((k+j)*20)][1]-9,pos[(19-(k+j+i))+((k+j)*20)][0]+9,pos[(19-(k+j+i))+((k+j)*20)][1]+9,fill="black")
                               infor[k+j][19-(k+j+i)]=10
                               return 0
                elif(bottom==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j+i][17-k+j]==10):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j+i][17-(k+j)]==0):
                               canvas.create_oval(pos[(17-(k+j))+((k+j+i)*20)][0]-9,pos[(17-(k+j))+((k+j+i)*20)][1]-9,pos[(17-(k+j))+((k+j+i)*20)][0]+9,pos[(17-(k+j))+((k+j+i)*20)][1]+9,fill="black")
                               infor[k+j+i][17-(k+j)]=10
                               return 0

        #가로 세로 3개 검사 방어
        for i in range(20):
            for j in range(16):
                low=0
                column=0
                for k in range(5):
                    if(infor[i][j+k]==1):
                        low+=1
                    elif(infor[j+k][i]==1):
                        column+=1
                if(low==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[i][j+k]==10):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[i][j+k]==0):
                                canvas.create_oval(pos[(k+j)+((i)*20)][0]-9,pos[(k+j)+((i)*20)][1]-9,pos[(k+j)+((i)*20)][0]+9,pos[(k+j)+((i)*20)][1]+9,fill="black")
                                infor[i][j+k]=10
                                return 0
                elif(column==3):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[j+k][i]==10):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[j+k][i]==0):
                                canvas.create_oval(pos[(i)+((k+j)*20)][0]-9,pos[(i)+((k+j)*20)][1]-9,pos[(i)+((k+j)*20)][0]+9,pos[(i)+((k+j)*20)][1]+9,fill="black")
                                infor[j+k][i]=10
                                return 0

        #대각선 2개 검사 공격
        for i in range(16):
            for j in range(16-i):
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][k+j+i]==10):
                        top+=1
                    elif(infor[k+j+i][k+j]==10):
                        bottom+=1
                if(top==2):
                    for k in range(5):
                        if(infor[k+j][k+j+i]==0):
                            canvas.create_oval(pos[(k+j+i)+((k+j)*20)][0]-9,pos[(k+j+i)+((k+j)*20)][1]-9,pos[(k+j+i)+((k+j)*20)][0]+9,pos[(k+j+i)+((k+j)*20)][1]+9,fill="black")
                            infor[k+j][k+j+i]=10
                            return 0
                elif(bottom==2):
                    for k in range(5):
                        if(infor[k+j+i][k+j]==0):
                            canvas.create_oval(pos[(k+j)+((k+j+i)*20)][0]-9,pos[(k+j)+((k+j+i)*20)][1]-9,pos[(k+j)+((k+j+i)*20)][0]+9,pos[(k+j)+((k+j+i)*20)][1]+9,fill="black")
                            infor[k+j+i][k+j]=10
                            return 0

                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][19-(k+j+i)]==10):
                        top+=1
                    elif(infor[k+j+i][19-(k+j)]==10):
                        bottom+=1
                if(top==2):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][19-(k+j+i)]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j][19-(k+j+i)]==0):
                               canvas.create_oval(pos[(19-(k+j+i))+((k+j)*20)][0]-9,pos[(19-(k+j+i))+((k+j)*20)][1]-9,pos[(19-(k+j+i))+((k+j)*20)][0]+9,pos[(19-(k+j+i))+((k+j)*20)][1]+9,fill="black")
                               infor[k+j][19-(k+j+i)]=10
                               return 0
                elif(bottom==2):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j+i][19-k+j]==1):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j+i][19-(k+j)]==0):
                               canvas.create_oval(pos[(19-(k+j))+((k+j+i)*20)][0]-9,pos[(19-(k+j))+((k+j+i)*20)][1]-9,pos[(19-(k+j))+((k+j+i)*20)][0]+9,pos[(19-(k+j))+((k+j+i)*20)][1]+9,fill="black")
                               infor[k+j+i][19-(k+j)]=10
                               return 0

        #가로 세로 2개 검사 공격
        for i in range(20):
            for j in range(16):
                low=0
                column=0
                for k in range(5):
                    if(infor[i][j+k]==10):
                        low+=1
                    elif(infor[j+k][i]==10):
                        column+=1
                if(low==2):
                    for k in range(5):
                        if(infor[i][j+k]==0):
                            canvas.create_oval(pos[(k+j)+(i*20)][0]-9,pos[(k+j)+(i*20)][1]-9,pos[(k+j)+(i*20)][0]+9,pos[(k+j)+(i*20)][1]+9,fill="black")
                            infor[i][j+k]=10
                            return 0
                elif(column==2):
                    for k in range(5):
                        if(infor[j+k][i]==0):
                            canvas.create_oval(pos[i+((k+j)*20)][0]-9,pos[i+((k+j)*20)][1]-9,pos[i+((k+j)*20)][0]+9,pos[i+((k+j)*20)][1]+9,fill="black")
                            infor[j+k][i]=10
                            return 0

                        
        #대각선 2개 검사 방어
        for i in range(16):
            for j in range(16-i):
                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][k+j+i]==1):
                        top+=1
                    elif(infor[k+j+i][k+j]==1):
                        bottom+=1
                if(top==2):
                    for k in range(5):
                        if(infor[k+j][k+j+i]==0):
                            canvas.create_oval(pos[(k+j+i)+((k+j)*20)][0]-9,pos[(k+j+i)+((k+j)*20)][1]-9,pos[(k+j+i)+((k+j)*20)][0]+9,pos[(k+j+i)+((k+j)*20)][1]+9,fill="black")
                            infor[k+j][k+j+i]=10
                            return 0
                elif(bottom==2):
                    for k in range(5):
                        if(infor[k+j+i][k+j]==0):
                            canvas.create_oval(pos[(k+j)+((k+j+i)*20)][0]-9,pos[(k+j)+((k+j+i)*20)][1]-9,pos[(k+j)+((k+j+i)*20)][0]+9,pos[(k+j)+((k+j+i)*20)][1]+9,fill="black")
                            infor[k+j+i][k+j]=10
                            return 0

                top=0
                bottom=0
                for k in range(5):
                    if(infor[k+j][19-(k+j+i)]==1):
                        top+=1
                    elif(infor[k+j+i][19-(k+j)]==1):
                        bottom+=1
                if(top==2):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j][19-(k+j+i)]==10):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j][19-(k+j+i)]==0):
                               canvas.create_oval(pos[(19-(k+j+i))+((k+j)*20)][0]-9,pos[(19-(k+j+i))+((k+j)*20)][1]-9,pos[(19-(k+j+i))+((k+j)*20)][0]+9,pos[(19-(k+j+i))+((k+j)*20)][1]+9,fill="black")
                               infor[k+j][19-(k+j+i)]=10
                               return 0
                elif(bottom==2):
                    apps=0
                    for k in range(5):
                        if(k>0 and k<4):
                            if(infor[k+j+i][19-k+j]==10):
                                continue
                            apps+=1
                    if(apps==3):
                        for k in range(5):
                            if(infor[k+j+i][19-(k+j)]==0):
                               canvas.create_oval(pos[(19-(k+j))+((k+j+i)*20)][0]-9,pos[(19-(k+j))+((k+j+i)*20)][1]-9,pos[(19-(k+j))+((k+j+i)*20)][0]+9,pos[(19-(k+j))+((k+j+i)*20)][1]+9,fill="black")
                               infor[k+j+i][19-(k+j)]=10
                               return 0

        #가로세로 2개 검사 방어
        for i in range(20):
            for j in range(16):
                low=0
                column=0
                for k in range(5):
                    if(infor[i][j+k]==1):
                        low+=1
                    elif(infor[j+k][i]==1):
                        column+=1
                if(low==2):
                    for k in range(5):
                        if(infor[i][j+k]==0):
                            canvas.create_oval(pos[(k+j)+(i*20)][0]-9,pos[(k+j)+(i*20)][1]-9,pos[(k+j)+(i*20)][0]+9,pos[(k+j)+(i*20)][1]+9,fill="black")
                            infor[i][j+k]=10
                            return 0
                elif(column==2):
                    for k in range(5):
                        if(infor[j+k][i]==0):
                            canvas.create_oval(pos[i+((k+j)*20)][0]-9,pos[i+((k+j)*20)][1]-9,pos[i+((k+j)*20)][0]+9,pos[i+((k+j)*20)][1]+9,fill="black")
                            infor[j+k][i]=10
                            return 0

        #수 없으면 수 창출
        for i in range(20):
            for j in range(20):
                if(infor[i][j]==10):
                    if(infor[i+1][j+1]==0):
                        canvas.create_oval(pos[(j+1)+((i+1)*20)][0]-9,pos[(j+1)+((i+1)*20)][1]-9,pos[(j+1)+((i+1)*20)][0]+9,pos[(j+1)+((i+1)*20)][1]+9,fill="black")
                        infor[i+1][j+1]=10
                        return 0
                    elif(infor[i][j+1]==0):
                        canvas.create_oval(pos[(j+1)+((i)*20)][0]-9,pos[(j+1)+((i)*20)][1]-9,pos[(j+1)+((i)*20)][0]+9,pos[(j+1)+((i)*20)][1]+9,fill="black")
                        infor[i][j+1]=10
                        return 0
                    elif(infor[i+1][j]==0):
                        canvas.create_oval(pos[(j)+((i+1)*20)][0]-9,pos[(j)+((i+1)*20)][1]-9,pos[(j)+((i+1)*20)][0]+9,pos[(j)+((i+1)*20)][1]+9,fill="black")
                        infor[i+1][j]=10
                        return 0
                    elif(infor[i-1][j-1]==0):
                        canvas.create_oval(pos[(j-1)+((i-1)*20)][0]-9,pos[(j-1)+((i-1)*20)][1]-9,pos[(j-1)+((i-1)*20)][0]+9,pos[(j-1)+((i-1)*20)][1]+9,fill="black")
                        infor[i-1][j-1]=10
                        return 0
                    elif(infor[i][j-1]==0):
                        canvas.create_oval(pos[(j-1)+((i)*20)][0]-9,pos[(j-1)+((i)*20)][1]-9,pos[(j-1)+((i)*20)][0]+9,pos[(j-1)+((i)*20)][1]+9,fill="black")
                        infor[i][j-1]=10
                        return 0
                    elif(infor[i-1][j]==0):
                        canvas.create_oval(pos[(j)+((i-1)*20)][0]-9,pos[(j)+((i-1)*20)][1]-9,pos[(j)+((i-1)*20)][0]+9,pos[(j)+((i-1)*20)][1]+9,fill="black")
                        infor[i-1][j]=10
                        return 0
                    elif(infor[i-1][j+1]==0):
                        canvas.create_oval(pos[(j+1)+((i-1)*20)][0]-9,pos[(j+1)+((i-1)*20)][1]-9,pos[(j+1)+((i-1)*20)][0]+9,pos[(j+1)+((i-1)*20)][1]+9,fill="black")
                        infor[i-1][j+1]=10
                        return 0
                    elif(infor[i+1][j-1]==0):
                        canvas.create_oval(pos[(j-1)+((i+1)*20)][0]-9,pos[(j-1)+((i+1)*20)][1]-9,pos[(j-1)+((i+1)*20)][0]+9,pos[(j-1)+((i+1)*20)][1]+9,fill="black")
                        infor[i+1][j-1]=10
                        return 0
    

canvas=Canvas(main,width=400,height=400,bg="#FFBF00")
canvas.pack()
omok=Omok(canvas,pos,random.randint(0,1))
omok.make_line()
computer()

while(1):
    canvas.bind("<Button-1>",omok.draw)
    canvas.bind("<Button-3>",omok.check)
    canvas.bind("<ButtonRelease-3>",omok.delete)

    main.mainloop()
