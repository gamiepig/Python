import pygame as py

py.init() #리셋,초기화

#빛의 3원색
Black=(0,0,0)
Red=(255,0,0)
Blue=(0,0,255)
Green=(0,255,0)
syan=(0,255,153)

size = [400,400] #[x,y]
screen = py.display.set_mode(size) #해상도 크기

py.display.set_caption("Rush")

done = False
clock = py.time.Clock()  # 프레임



while not done:

      clock.tick(10)
      print("replaying")
      for event in py.event.get(): 
            if event.type == py.QUIT:
              done = True







      screen.fill(syan)

      py.draw.rect(screen,Black,[200,200,100,100],2)
      #[x,y 좌표 , 가로세로 길이]
      py.draw.polygon(screen,Blue,[[150,200],[250,130],[350,200]])
      py.draw.circle(screen,Red,[355,30],30)
      py.draw.line(screen,Black,[250,240],[279,240],2)
      py.draw.line(screen,Black,[250,240],[279,240],2)
      py.draw.line(screen,Black,[265,225],[265,254],2)
      py.draw.rect(screen,Black,[250,225,29,29],2)
      py.display.flip()
              
              
