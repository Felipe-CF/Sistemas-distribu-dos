import pygame
from pygame.locals import *


class Quadrado(pygame.sprite.Sprite):

    def __init__(self):
        super(Quadrado, self).__init__()

        # cria a superficia retangular (surf) para desenhar o quadrado
        self.surf = pygame.Surface((25, 25))

        # preenche surf de verde
        self.surf.fill((34, 139, 34))
        
        # cria um retangulo (pygame.Rect) que envolve a superficie
        # importante para manipular a posição do sprite e detectar colisões
        self.rect = self.surf.get_rect()


pygame.init()

# display do jogo
tela = pygame.display.set_mode((800, 600))

square1 = Quadrado()
square2 = Quadrado()
square3 = Quadrado()
square4 = Quadrado()
 
# variavel que mantem o jogo rodando
gameOn = True
 
# loop que mantem o jogo
while gameOn:

    # retorna uma lista de eventos que ocorreram desde o último ciclo do loop
    for event in pygame.event.get():
         
        # checa se uma tecla foi pressionada
        if event.type == KEYDOWN:
             
            # checa se a tecla foi "backspace"
            if event.key == K_BACKSPACE:
                gameOn = False # sai do loop
                 
        # checa se, por exemplo, a janela foi fechada 
        elif event.type == QUIT:
            gameOn = False
 
    # Define onde os quadrados vão aparecer na tela
    # o blit desenha eles na superficie onde o jogo roda to draw them on the screen surface
    tela.blit(square1.surf, (40, 40))
    tela.blit(square2.surf, (40, 530))
    tela.blit(square3.surf, (730, 40))
    tela.blit(square4.surf, (730, 530))
 
    # atualiza o display com as mudanças feitas
    pygame.display.flip()

