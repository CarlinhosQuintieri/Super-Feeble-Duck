import pygame
from pygame import font
from pygame.locals import *
from sys import exit
from pygame import mixer
mixer.init()
pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 60)
Img = pygame.image.load('over.jpg')
Img = pygame.transform.scale(Img, (800, 600))
Img2 = pygame.image.load('jogin2.png')
Img2 = pygame.transform.scale(Img2, (800, 500))
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE)
def over():
    cont=0
    while True:
        clock.tick(1)
        mixer.music.load('Fquack.mp3')
        mixer.music.play()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key==K_SPACE:
                    pygame.mixer.music.load('Fquack-quack.mp3')
                    pygame.mixer.music.play(0)
        screen.fill((255,255,255))
        screen.blit(Img,(0,0))
        cont+=1
        if(cont%2==0):
            screen.blit(Img2,(0,50))
        pygame.display.update()
pass
over()


