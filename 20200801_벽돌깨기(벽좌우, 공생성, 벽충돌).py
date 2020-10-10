import pygame as p

p.init()#초기화

s=(600,800) #(가로세로)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("벽돌깨기")

playing = True

pan = p.image.load("pan.png")
p_rect = pan.get_rect(left = 250 , top = 730)
px = 0
#배경
bg = p.image.load("bg2.png")
#공
ball = p.image.load("ball.png")
bl_rect = ball.get_rect(left = 270, top = 370)
#공 스피드 관련 변수
bx = 8
by = 8
#게임오버
font = p.font.SysFont("malgungothic",50)

#벽돌 생성
block = p.image.load("bl.png")
block_list = []
for x in range(10):
    for y in range(5):
        blo_rect = block.get_rect(left = 60*x, top = 50*y)
        block_list.append(blo_rect)
    
#점수 생성    
score = 0
font1 = p.font.SysFont("malgungothic",20)
  
while playing:

    for event in p.event.get():
        if event.type == p.QUIT:    
            playing =False
            p.quit()
            quit()

        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                px = -8
            if event.key == p.K_RIGHT:
                px = 8

        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                px = 0
            if event.key == p.K_RIGHT:
                px = 0

    p_rect.left += px


    sc.fill(white)
    sc.blit(bg,(0,0))
    sc.blit(pan,p_rect)
    if p_rect.left >= 500:
        p_rect.left = 500
    if p_rect.left <= 0:
          p_rect.left = 0
    sc.blit(ball,bl_rect)
    #공 움직이기
    bl_rect.top += by
    if bl_rect.top >=770:
        by = -by
    if bl_rect.top <=0:
        by = -by

    bl_rect.left += bx
    if bl_rect.left >=570:
        bx = -bx
    if bl_rect.left <=0:
        bx = -bx

    text = font.render("GameOver",True,(0,0,255))

    if bl_rect.top >=770:
         sc.blit(text,(170,350))
         playing = False


    if p_rect.colliderect(bl_rect):
        by = -4

       

    for blo_rect in block_list:
        sc.blit(block,blo_rect)

    for blo_rect in block_list:
        if blo_rect.colliderect(bl_rect):
            block_list.remove(blo_rect)
            by = 4
            score += 1
            
   #점수 업로드
    text1 = font1.render("점수 : {}".format(score),True,(255,255,0))
    sc.blit(text1,(1,770))

    
    #clear
    text2 = font.render("Clear",True,(0,0,255))
    if (len(block_list)) <= 0:
        sc.blit(text2,(170,350))
        playing = False
    
 
    p.display.flip()
            
            
    
