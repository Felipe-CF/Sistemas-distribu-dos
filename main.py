import pygame
from pygame.locals import *
from quadrado import Quadrado
from matriz import Matriz


matriz_binaria = Matriz.maatriz()

pygame.init()

# display do jogo
tela = pygame.display.set_mode((800, 600))

lotes = pygame.sprite.Group()

fundo = pygame.image.load("campo.png")

tela.blit(fundo, (0, 0))
 
# variavel que mantem o jogo rodando
gameOn = True

# loop que mantem o jogo
while gameOn:

    Matriz.gera_campo_minado(x_ref=40, y_ref=40, tela=tela, matriz_binaria=matriz_binaria, aresta=25, lotes=lotes)

    # retorna uma lista de eventos que ocorreram desde o último ciclo do loop
    for evento in pygame.event.get():

        # checa se uma tecla foi pressionada
        if evento.type == KEYDOWN:
             
            # checa se a tecla foi "backspace"
            if evento.key == K_BACKSPACE:
                gameOn = False # sai do loop
        

                 
        # checa se, por exemplo, a janela foi fechada 
        elif evento.type == QUIT:
            gameOn = False

    lotes.draw(tela)
    pygame.display.flip()

pygame.quit()


# elif evento.type == pygame.MOUSEBUTTONUP: # se o evento foi o clique do mouse

#     #pego a posicao dele
#     posicao_mouse = pygame.mouse.get_pos()

#     # verifico em qual quadrado ocorreu o clique
#     lotes_clicados = [lote for lote in lotes if lote.rect.collidepoint(posicao_mouse)]

#     # teste para pintar de branco o lote clicado
#     for lote in lotes_clicados:
#         lote.surf.fill((255, 255, 255))
