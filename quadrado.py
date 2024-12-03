import pygame
from pygame.locals import *


class Quadrado(pygame.sprite.Sprite):

    def __init__(self, aresta):

        super(Quadrado, self).__init__()

        self.aresta = aresta

        # cria a superficia retangular (surf) para desenhar o quadrado
        self.surf = pygame.Surface((aresta, aresta))

        # branco inicial
        self.surf.fill((255, 255, 255))
        
        # cria um retangulo (pygame.Rect) que envolve a superficie
        # importante para manipular a posição do sprite e detectar colisões
        self.rect = self.surf.get_rect()

    def aresta(self):
        return self.aresta
    
    def altera_cor(self, r, g, b):
        self.surf.fill((r, g, b))