import pygame as p

p.init() # 라이브러리 초기화
size = (400,400) #가로,세로
sc = p.display.set_mode(size)#해상도 설정
p.display.set_caption("키보드 조작")
w = (255,255,255) #(R,G,B) 빛의 3원색(흰색)
b = (0,0,0)
#동그라미 좌표
x = 100
y = 100
playing = True

while playing:
    for event in p.event.get():#사용자가 뭘 누르는지 확인
        if event.type==p.QUIT:#만약 게임창 x버튼을 누른다면
            playing = False # 계속반복을 종료
            p.quit()#게임창 종료
            quit #sell 창 종료


        if event.type == p.KEYDOWN: #키보드를 눌렀을 떄 반응
            if event.key == p.K_UP :# 위 방향키를 누를 떄
                print("위 방향키 눌렀습니다")
                y = y-5
            if event.key == p.K_DOWN :
                print("아래 방향키 눌렀습니다")
                y = y+5
            if event.key == p.K_RIGHT :
                print("오른쪽 방향키 눌렀습니다")
                x = x+5
            if event.key == p.K_LEFT :
                print("왼쪽 방향키 눌렀습니다")
                x = x-5

                
        if event.type == p.KEYUP: #키보드를 눌렀을 떄 반응
            if event.key == p.K_UP :# 
                print("위 방향키 때었습니다")
            if event.key == p.K_DOWN :# 
                print("아래 방향키 때었습니다")
            if event.key == p.K_RIGHT :# 
                print("오른쪽 방향키 때었습니다")
            if event.key == p.K_LEFT :# 
                print("왼쪽 방향키 때었습니다")        



    sc.fill(w) #바탕화면 흰색
    p.draw.circle(sc,b,(x,y),40) #(x좌표,y좌표),반지름,선굵기
    p.display.flip()#화면 업데이트


