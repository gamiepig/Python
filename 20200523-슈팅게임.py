import pygame as p
import random as r

p.init() # 라이브러리 초기화
size = (800,400) #가로,세로
sc = p.display.set_mode(size)#해상도 설정
p.display.set_caption("키보드 조작")
w = (255,255,255) #(R,G,B) 빛의 3원색(흰색)
b = (0,0,0)
#이미지 변수에 옮기기
s = p.image.load("spa2.png")
h = p.image.load("han.png")
t = p.image.load("tai.png")
a = p.image.load("abc.png")
h_rect = h.get_rect(left = 10, top = 10)#left = x , top y 
bg_rect = s.get_rect(left = 0,top = 0) #원본배경좌표

bg_1 = s.copy()
bg1_rect = bg_1.get_rect(left = 800,top = 0)

t_1 = p.image.load("tai.png")
en_rect = t_1.get_rect(left = 700,top = 0)

#텍스트
font = p.font.SysFont('malgungothic',20)
font1 = p.font.SysFont('malgungothic',50)       
#비행기 좌표
x=25
y=0
y_1=0
playing = True
#배경 좌표
s_1 = 0
s1_1 = 800
#적군 좌표
en_x = 700
en_y = 0
#점수
score = 0

while playing:
    for event in p.event.get():#사용자가 뭘 누르는지 확인
        if event.type==p.QUIT:#만약 게임창 x버튼을 누른다면
            playing = False # 계속반복을 종료
            p.quit()#게임창 종료
            quit #sell 창 종료


        if event.type == p.KEYDOWN: #키보드를 눌렀을 떄 반응
            if event.key == p.K_UP :# 위 방향키를 누를 떄
                print("위 방향키 눌렀습니다")
                y = y+-5
            if event.key == p.K_DOWN :
                print("아래 방향키 눌렀습니다")
                y = +5
            

                
        if event.type == p.KEYUP: #키보드를 눌렀을 떄 반응
            if event.key == p.K_UP or event.key == p.K_DOWN : 
                y=0


    h_rect.top +=y
                    


    y_1 += y
    sc.fill(w) #바탕화면 흰색
    sc.blit(s,bg_rect)#배경
    sc.blit(bg_1,bg1_rect)
    bg_rect.left -= 2
    bg1_rect.left -= 2
    if bg_rect.left <= -800:
        bg_rect.left = 800
    if bg1_rect.left <= -800:
        bg1_rect.left = 800
    sc.blit(h,h_rect)#비행기 이미지 화면에 업로드

    if h_rect.top> 330:
        y = 0
    if h_rect.top<0 :
        y = 0
    sc.blit(t_1,en_rect)
    en_rect.left -= 14
    if en_rect.left <= -100:
        en_rect.left = 800
        en_rect.top = r.randint(0,325)
        score += 1


    text = font.render("점수:{}".format(score),True,(255,255,0))
    text1 = font1.render('GAME OVER',True,(0,255,255))
    sc.blit(text,(400,0))



    if h_rect.colliderect(en_rect):
        sc.blit(a,h_rect)
        sc.blit(text1,(250,150))
        playing = False
        

    
    p.display.flip()#화면 업데이트


