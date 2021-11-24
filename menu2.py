import pygame
from pygame import font
from pygame.locals import *
from sys import exit
from pygame import mixer
mixer.init()
mixer.music.load('Adventure.mp3')
mixer.music.play()
pygame.init()
clock = pygame.time.Clock()
txt = ('Pressione "espaço" para começar')
pygame.font.init()
fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 60)
#txtela = fontesys.render(txt, 1, (000,000,000))
Img = pygame.image.load('feeble cenário.png')
txtela = pygame.image.load('8-bit.png')
Img = pygame.transform.scale(Img, (800, 600))
Img2 = pygame.image.load('jogin.png')
Img2 = pygame.transform.scale(Img2, (800, 500))
Img3 = pygame.image.load('jogin.png')
Img3 = pygame.transform.scale(Img3, (800, 500))
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE)
def start():
    print("inicio do jogo")
    pass
cont=0

while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_SPACE:
                start()
                pygame.mixer.music.load('quack-quack.mp3')
                pygame.mixer.music.play(0)
    screen.fill((255,255,255))
    screen.blit(Img,(0,0))
    screen.blit(txtela,(100,500))
    cont+=1
    if(cont%2==0):
        screen.blit(Img3,(0,50))
    pygame.display.update()
