#Feito por Carlos Eduardo Saraiva Quintieri
import pygame,sys
from random import *
from pygame.locals import *
from pygame import mixer

width = 850
height = 570
x=70
y=200
x_change=0
y_change=0
gravidade=2.5
velocidade_jogo = 1
vivo = True
placar = 0
minutes = 0
seconds = 0
cont=0
Img = pygame.image.load('over.jpg')
Img = pygame.transform.scale(Img, (850, 600))
Img2 = pygame.image.load('jogin2.png')
Img2 = pygame.transform.scale(Img2, (850, 500))
Img3 = pygame.image.load('jogin.png')
Img3 = pygame.transform.scale(Img3, (800, 500))
clock = pygame.time.Clock()
txt = ('Pressione "espaço" para começar')
pygame.init()
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1) 
pygame.font.init()
fonte=pygame.font.get_default_font()
fontesys=pygame.font.SysFont(fonte, 60)
txtela = fontesys.render(txt, 1, (000,000,000))
WHITE = (255,255,255)
BLACK=(0,0,0)


def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,500))
    screen.blit(floor_surface,(floor_x_pos + 850,500))

def draw_tree():
    screen.blit(arvore_surface,(floor_x_pos, 350))

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
        screen.fill((255,255,255))
        screen.blit(Img,(0,0))
        cont+=1
        if(cont%2==0):
            screen.blit(Img2,(0,50))
        pygame.display.update()

screen = pygame.display.set_mode((width,height))
font = pygame.font.SysFont('sans',40)

#tela de pause
pause = pygame.image.load('Pause.png')
pause1=False
def paused():
    pygame.time.delay(0)
    screen.blit(pause, (200, 250))
    mixer.init()
    mixer.music.load('Adventure.mp3')
    mixer.music.play()
    pygame.display.flip()

#projeteis do jogo
disparo_surface = pygame.image.load('disparo.png')
disparo_surface = pygame.transform.scale(disparo_surface,(50,20))
disparo = True
xVermelho = 0
yVermelho = 0

#fundo
bg_surface = pygame.image.load('background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

pygame.draw.polygon(screen, WHITE, [(0, 0), (50, 100), (100, 0)])


#chão e regulagem da imagem
floor_surface = pygame.image.load('floor.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

#obstaculo do chão
arvore_surface = pygame.image.load('arvore.png')
arvore_surface = pygame.transform.scale(arvore_surface,(200,200))
arvore_rect = arvore_surface.get_rect(center=(850,450))

#personagem e regulagem da imagem
duck_surface = pygame.image.load('skate_duck.png')
duck_surface = pygame.transform.scale(duck_surface,(80,80))
def test(x,y):
    screen.blit(duck_surface,duck_rect)
duck_rect = duck_surface.get_rect(center=(x,y))

Start = True
while Start == True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key==K_SPACE:
                pygame.mixer.music.load('quack-quack.mp3')
                pygame.mixer.music.play(0)
                Start = False
    screen.fill((255,255,255))
    screen.blit(bg_surface,(0,0))
    screen.blit(txtela,(100,500))
    cont+=1
    if(cont%2==0):
        screen.blit(Img3,(0,50))
    pygame.display.update()

while vivo == True:
    clock.tick(60)
    #end = time.time()
    temporizador = ("{:0>2}:{:0>2}".format(int(minutes),int(seconds)))
    seconds = seconds+1
    print(velocidade_jogo)
    if (seconds == 100):
        placar+=100
        velocidade_jogo +=1
        seconds = 0
    elif(velocidade_jogo >= 16):
        velocidade_jogo -=1
    screen.blit(bg_surface,(0,0))    
    #nao passa do chão
    if duck_rect.y > height - 155:
        duck_rect.y = height - 155
    elif duck_rect.y < 0:
        duck_rect.y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #movimentação do pato, feita pelo jogador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_change=-2.5*gravidade
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                y_change=2*gravidade
        if event.type == pygame.KEYDOWN:
            if event.key == K_p:
                    paused()
                    pause1 = True
        while pause1 == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_p:
                        screen.fill(WHITE)
                        pygame.mixer.music.stop()
                        pause1 = False
    #menu?
    #blita o pato
    test(x,y)
    score1 = font.render('Pontuação: '+str(placar), True, (BLACK))
    screen.blit(score1, (500, 50))
    #timer1 = font.render('Tempo ' + str(temporizador), True, (BLACK))
    #screen.blit(timer1, (30, 50))
    screen.blit(arvore_surface,arvore_rect)
    #disparos
    if disparo == True:
        xVermelho = randint(10,450)
        yVermelho = 850
        disparo = False
    yVermelho -= velocidade_jogo * 1.5
    posicaoDisparo = [yVermelho,xVermelho]
    if yVermelho <1:
        disparo = True
    disparo_rect = disparo_surface.get_rect(topleft=(yVermelho,xVermelho))
    #pygame.draw.rect(screen,(0,255,0),arvore_rect,4)
    #colisao do disparo
    if duck_rect.colliderect(disparo_rect):
        disparo = True
        over()
    #colisao arvore
    if duck_rect.colliderect(arvore_rect):
        over()
    #movimentação do pato
    duck_rect.y+=y_change
    #chão
    floor_x_pos -=velocidade_jogo * 1
    arvore_rect.x -= velocidade_jogo * 1
    draw_floor()
    #draw_tree()
    screen.blit(disparo_surface,(posicaoDisparo))
    #screen.blit(arvore_surface,arvore_rect)
    if floor_x_pos <= -850:
        floor_x_pos = 0
    if arvore_rect.x <= -200:
        arvore_rect.x = 850
    
    pygame.display.update()