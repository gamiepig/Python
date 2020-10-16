import pygame as p
import random as r

p.init()#라이브러리 초기화
w = (255,255,255)
size = (800,400)#(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True
m = p.image.load("money.png")
m_rect = m.get_rect(left = r.randint(0,700),top = r.randint(0,300))
font = p.font.SysFont("malgungothic",20)
score = 0



while playing:#계속 반복
    for event in p.event.get():#사용자가 뭘 누르는 지 검사
        if event.type == p.QUIT:#게임창 s를 누르면
            playing = False #계속 반복을 종료
            p.quit()#게임창 종료
            quit()#SELL창 종료
        if event.type == p.MOUSEBUTTONDOWN:#마우스 클릭했을때
            if m_rect.collidepoint(event.pos[0],event.pos[1]):#돈과 마우스 포인터가 충돌했는가
                m_rect = m.get_rect(left = r.randint(0,700),top = r.randint(0,300))
                score += 1
            
        
            print("마우스 클릭해습니다")
            print("x =",event.pos[0],"y =",event.pos[1])
        if event.type == p.MOUSEBUTTONUP:#마우스 땠을때
            print("마우스 떄었습니다")  

    sc.fill(w)
    sc.blit(m,m_rect)
    text = font.render("점수: {}".format(score),True,(0,0,0))
    sc.blit(text,(365,0))

    p.display.flip()#화면 업데이트
    
            
