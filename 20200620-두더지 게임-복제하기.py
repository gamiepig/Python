import pygame as p
import random as r

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
while playing:#계속 반복
    for event in p.event.get():#사용자가 뭘 누르는 지 검사
        if event.type == p.QUIT:#게임창 s를 누르면
            playing = False #계속 반복을 종료
            p.quit()#게임창 종료
            quit()#SELL창 종료

    sc.fill(w)
    for do_rect in do_list:
        sc.blit(do,do_rect)
    p.display.flip()#화면 업데이트
            
