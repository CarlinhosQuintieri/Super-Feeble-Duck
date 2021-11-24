import sys, pygame
from pygame.locals import *
from random import *
import time
from pygame import mixer
pygame.init()
clock = pygame.time.Clock()
vivo = True
size = (800, 600)
screen = pygame.display.set_mode(size)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK=(0,0,0)
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1) 
font = pygame.font.SysFont('sans',40)
placar = 0
minutes = 0
seconds = 0
cont=0
pause = pygame.image.load('pause.png')
pause1=False
def paused():
    pygame.time.delay(3000)
    screen.blit(pause, (200, 250))
    mixer.init()
    mixer.music.load('Adventure.mp3')
    mixer.music.play()
    pygame.display.flip()
while vivo == True:
    clock.tick(1)
    temporizador = ("{:0>2}:{:0>2}".format(int(minutes),int(seconds)))
    screen.fill(WHITE)
    seconds = seconds+1
    cont+=1
    if(seconds==60):
        seconds=0
        minutes+=1
    if (cont==10):
        placar+=100
        cont=0
    score1 = font.render('Pontuação: '+str(placar), True, (BLACK))
    screen.blit(score1, (500, 50))
    timer1 = font.render('Tempo ' + str(temporizador), True, (BLACK))
    screen.blit(timer1, (30, 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_p:
                paused()
                pause1 = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    while pause1 == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    screen.fill(WHITE)
                    pygame.mixer.music.stop()
                    pause1 = False
            
