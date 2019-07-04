import pygame
import sys
import random
import pygame.freetype
pygame.init()
pygame.mixer_music.load('mk.mp3')
size=width,height=600,400
speed=[0,0,0,1]
Black=0,0,0
screen=pygame.display.set_mode(size)
pygame.display.set_caption('tankwar')
tank=pygame.image.load('up.tank.png')
tankrect=tank.get_rect()
tankrect.left=200
tankrect.top=330
enemy_tank1=pygame.image.load('down.tank.png')
enemy_tank1rect=enemy_tank1.get_rect()
enemy_tank1rect.left=400
enemy_tank1rect.top=50
bullet=pygame.image.load('bullet.tank.png')
bulletrect1=bullet.get_rect()
bulletrect1.left=tankrect.left+15
bulletrect1.top=tankrect.top-15
bulletrect2=bullet.get_rect()
bulletrect2.left=enemy_tank1rect.left+20
bulletrect2.top=enemy_tank1rect.top+12
oldpostion=enemy_tank1rect.left,enemy_tank1rect.top
k=1
kill=0
pygame.mixer_music.play()
bgcolor=pygame.Color('black')
f1=pygame.freetype.Font('C://Windows//Fonts//msyh.ttc',36)
GOLD=255,251,0
f1surf,f1rect=f1.render('小键盘和空格进行行走和开火',fgcolor=GOLD,size=10)
def fut(a):
    if a==0:
        a=random.randint(1,255)
    return a

def RGBchannel(a):
    return 1 if a<=0 else(255 if a>255 else int(a))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed[0]=speed[0]-1
            elif event.key==pygame.K_RIGHT:
                speed[0]=speed[0]+1
            elif event.key==pygame.K_UP:
                speed[1]=speed[1]-1
            elif event.key==pygame.K_DOWN:
                speed[1]=speed[1]+1
            elif event.key==pygame.K_SPACE:
                speed[2]=speed[2]-1
            elif event.type==pygame.VIDEORESIZE:
                size=width,height=event.size[0],event.size[1]
                screen=pygame.display.set_mode(size,pygame.RESIZABLE)


    tankrect=tankrect.move(speed[0],speed[1])
    bulletrect1=bulletrect1.move(0,speed[2])
    bulletrect2=bulletrect2.move(0,speed[3])

    if tankrect.left<0 or tankrect.right>width:
        speed[0]=0
    if tankrect.top<0 or tankrect.bottom>height:
        speed[1]=0
    if bulletrect1.top<0:
        bulletrect1.top=tankrect.top
        bulletrect1.left=tankrect.left+15
    if bulletrect1.top==enemy_tank1rect.top and enemy_tank1rect.right>bulletrect1.left>enemy_tank1rect.left:
        enemy_tank1=pygame.image.load('images.gif')
        speed[3]=0
        bulletrect2.top=-20
        enemy_tank1rect.left,enemy_tank1rect.top=oldpostion
    if bulletrect2.top==tankrect.top and tankrect.left<bulletrect2.left<tankrect.right:
        tank=pygame.image.load('gg.png')
        bulletrect1.top=0
        speed[2]=0

    if bulletrect2.top>400:
        bulletrect2.top=enemy_tank1rect.top+10
        bulletrect2.left=enemy_tank1rect.left+10

    bgcolor.r=RGBchannel(tankrect.left*255/width)
    bgcolor.g=RGBchannel(tankrect.top*255/width)
    bgcolor.b=RGBchannel(min(speed[0],speed[1])*255/fut(max(speed[0],speed[1])))
    r=random.randint(0,4)
    k+=1

    if k<200:
            enemy_tank1rect.left, enemy_tank1rect.top = oldpostion
    if 200<k<400:
            enemy_tank1rect.left+=0.1
    elif 400<k<600:

            enemy_tank1rect.top+=0.1

    elif 600<k<800:
        enemy_tank1rect.top-=0.1
    elif 800<k<850 :
        enemy_tank1rect.left-=0.1
    elif 850<k<2000:
        enemy_tank1rect.left+=0.1
        oldpostion=enemy_tank1rect.left, enemy_tank1rect.top
    if k>2000:
        k=1
    r1rect=pygame.draw.rect(screen,bgcolor,(210,210,200,100),5)


    screen.fill(Black)
    screen.blit(tank,tankrect)
    screen.blit(enemy_tank1,enemy_tank1rect)
    screen.blit(f1surf,(20,20))
    screen.blit(bullet,bulletrect1)
    screen.blit(bullet,bulletrect2)
    pygame.display.update()


