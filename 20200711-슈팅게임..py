import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #흰색 RGB
size = (600,900)#(가로,세로)
sc = p.display.set_mode(size)   
p.display.set_caption("슈팅게임")
playing = True
#비행기
p_image = p.image.load("s.png")
p_rect = p_image.get_rect(left=260 ,top=800)
x =0
y =0
#배경
bg = p.image.load("BG.png")
#미사일
b_image = p.image.load("a.png")
b_list = [ ]


while playing: #while True-게속반복

    for event in p.event.get(): #사용자 무엇을 누르는지 검사
        if event.type == p.QUIT: #게임창 x버튼을 누른다면
            playing = False
            p.quit() #게임창 끔
            quit() #sell창 종료

        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                y = -3
            if event.key == p.K_DOWN:
                y = 3
            if event.key == p.K_LEFT:
                x = -3
            if event.key == p.K_RIGHT:
                x = 3
            if event.key == p.K_SPACE:
                b_rect = b_image.get_rect(left=p_rect.left + 35, top=p_rect.top)
                b_list.append(b_rect)
                
        if event.type == p.KEYUP:
            if event.key == p.K_UP:
                y = 0
            if event.key == p.K_DOWN:
                y = 0
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0

    p_rect.left += x # += --> p.rect.left = p.rect.left + x
    p_rect.top += y
     
    sc.fill(white) #배경화면 색설정
    sc.blit(bg,(0,0))
    for b_rect in b_list:
        sc.blit(b_image,b_rect)
    for b_rect in b_list:
        b_rect.top -= 5
    sc.blit(p_image,p_rect)
    p.display.flip() #화면 업데이트
    
