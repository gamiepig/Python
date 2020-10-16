import pygame as p

p.init#초기화

s=(800,400)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("선생님의 요구")

playing = True

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()


    sc.fill(white)
    p.display.flip()
            
            
    
