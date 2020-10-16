import pygame as p
import random as r
import time as t

p.init()#라이브러리 초기화
w = (255,255,255)
size = (800,400)#(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True
do = p.image.load("두더지 (2).png")
do_list = []
for x in range(10):
    do_rect = do.get_rect(left = r.randint(0,700),top = r.randint(0,300))
    do_list.append(do_rect)
    
font = p.font.SysFont('malgungothic',20)
score = 0
#남은 시간
t1 = int(t.time())#멈춘 시간

p.mixer.init()#초기화
hit = p.mixer.Sound("h.wav")

while playing:#계속 반복
    t2 = int(t.time())#흐르는 시간
    timer = 60 - (t2 - t1)
    print (timer)
    for event in p.event.get():#사용자가 뭘 누르는 지 검사
        if event.type == p.QUIT:#게임창 s를 누르면
            playing = False #계속 반복을 종료
            p.quit()#게임창 종료
            quit()#SELL창 종료
        if event.type == p.MOUSEBUTTONDOWN:#마우스 버튼을 클릭했을때:
            for do_rect in do_list:
                if do_rect.collidepoint(event.pos[0],event.pos[1]):
                    do_list.remove(do_rect)
                    do_rect = do.get_rect(left = r.randint(0,700),top = r.randint(0,300))
                    score += 1 #score = score +1
                    hit.play()

                    

                    do_list.append(do_rect)
                    #두더지 좌표 재배치
                    #두더지 리스트 업로드

    sc.fill(w)
    for do_rect in do_list:
        sc.blit(do,do_rect)

    if timer == 0:
        playing = False

    text = font.render("점수:{}".format(score),True,(0,0,0))
    sc.blit(text,(375,0))
    text1 = font.render("남은 시간:{}".format(timer),True,(0,0,0))
    sc.blit(text1,(675,0))
    
    p.display.flip()#화면 업데이트
            
