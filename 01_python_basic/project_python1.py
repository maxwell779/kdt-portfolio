''' TKinter에서 구현된 GUI 환경에서 파일을 불러들이고 
    불러온 파일의 숫자의 총합, 평균, 중앙값을 구하고
    문자,숫자, 공백의 갯수를 입력할 수 있는 버튼을 구현
    추가된 문자를 다른 파일에 저장할 수 있는 버튼도 구현'''

from tkinter import *


#함수 설정

def readfile(): # 입력된 file 경로를 통해 파일을 불러오는 함수
    global numlist
    global sum
    global lines2
    filename = ent1.get() #ent1에 적혀 있는 경로로 파일명 부여
    with open(filename,'r') as file:
        lines = file.readlines() # lines에 readlines로 리스트로 변환
        lines2 = "".join(lines) # 다시 하나의 문자열로 합침
        txt1.insert(END,lines2) # text에 문자열 입력
        txtlist = lines2.split(',') # txt list에 ','로 분리된 리스트 입력 후 
        numlist = list(int(s) for s in txtlist if s.isdigit()) # 숫자 인것만 대입
        file.close()

        
def filemake(): # 입력된 file명에 대해 입력된 text를 파일로 저장하는 함수
    filename2 = ent2.get()
    txt = txt1.get("1.0","end-1c") # txt에 txt1에 입력된 모든 문자를 저장
    with open(filename2,'w') as file:
        file.writelines(txt) # 모든 문자 입력
        file.close()     
        
def sum2(): # 총 합을 찾아내는 함수
    global sum
    sum = 0
    for i in numlist:
        sum += i
    print(sum)
    txt1.insert(END,'\n'+'총 합: '+ str(sum))
    
def average(): # 평균을 찾아내는 함수
    global sum
    global numlist
    average = sum/len(numlist)
    txt1.insert(END,'\n'+'평균'+str(average))
    
def centernum(): # 중앙값을 찾아내는 함수
    global numlist
    numlist.sort()
    center = numlist[len(numlist)//2]
    txt1.insert(END,'\n'+'중앙값'+str(center))
    return center

def isalnum(): # 문자, 숫자, 공백 갯수를 찾아내는 함수
    global count_al
    global count_num
    global lines2
    count_al = 0
    count_num = 0
    count_space = 0
    
    for i in lines2:
        if i.isdigit():
            count_num += 1
        elif i.isalpha():
            count_al += 1
        elif i.isspace():
            count_space += 1
            
    print(count_al,count_num)
    txt1.insert(END,'\n문자 갯수:'+str(count_al))
    txt1.insert(END,'\n숫자 갯수:'+str(count_num))
    txt1.insert(END,'\n공백 갯수:'+str(count_space))

# 메인 함수
window = Tk()
window.geometry("1000x600")
window.configure(bg = 'yellow') # 배경을 빨간색으로 설정
window.title("문서 분석하기")

# 위젯 생성
lab1 = Label(window, text = "문서 불러온 후 분석하기", font = ("맑은 고딕",30),fg = "blue")
ent1 = Entry(window, width = 30)
ent1.insert(END,'파일명을 입력하세요.')
ent2 = Entry(window,width = 30)
ent2.insert(END,'파일명을 입력하세요.')
txt1 = Text(window, width = 100, height = 50)
btn1 = Button(window, text = '파일 경로 입력', bg = "green", font = ("맑은 고딕",12), width = 15, command = readfile)
btn2 = Button(window, text = '파일 생성' , bg = "green", font = ("맑은 고딕",12),width = 15, command = filemake)
btn3 = Button(window, text = '총합' , bg = "green", font = ("맑은 고딕",12),width = 15, command = sum2)
btn4 = Button(window, text = '평균' , bg = "green", font = ("맑은 고딕",12),width = 15, command = average)
btn5 = Button(window, text = '중앙값' , bg = "green", font = ("맑은 고딕",12),width = 15, command = centernum)
btn6 = Button(window, text = '문자, 숫자 개수', bg = "green", font = ("맑은 고딕",12),width = 15,  command = isalnum)


# 위젯 위치 설정
lab1.place(x = 350, y =30)
ent1.place(x = 250, y = 100)
ent2.place(x = 250, y = 150)
txt1.place(x = 250, y = 200)
btn1.place(x = 60, y = 100)
btn2.place(x = 60, y = 150)
btn3.place(x = 60, y = 300)
btn4.place(x = 60, y = 350)
btn5.place(x = 60, y = 400)
btn6.place(x = 60, y = 450)

window.mainloop()
