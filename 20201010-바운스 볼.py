import pygame as p

p.init()#초기화
s=(1000,600)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("bounce_ball")

playing = True
#공 이미지 업로드
ball = p.image.load("bar.png")
b_rect = ball.get_rect(left = 470, top = 270)
b_x = 0
b_y = 3 #중력 비슷한 역할
#fps
clock = p.time.Clock()
#수정
while playing:
    clock.tick(60)

    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()


    sc.fill(white)
    sc.blit(ball,(b_rect))
    #공 밑으로 내리기
    b_rect.top += b_y
    b_y += 1

    if b_rect.top >= 570:
        b_y = -20

        
    p.display.flip()
            
            
    
