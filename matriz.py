import random
from quadrado import Quadrado
from pygame.locals import *

class Matriz:

    # matriz servidor
    def gera_matriz(): 

        # quantidade de bombas por partida
        bombas = 5

        matriz_r = []

        for i in range(0, 5):

            matriz_c = []

            for j in range(0, 5):

                if random.randint(0, 1) == 0 and bombas > 0:

                    matriz_c.append(0)

                    bombas -= 1

                else:
                    matriz_c.append(1)

            matriz_r.append(matriz_c)
        
        return matriz_r


    def atualiza_matriz(linha, coluna, matriz):
        
        if matriz[linha][coluna] == 2:

            return "escolhido", matriz
        
        elif matriz[linha][coluna] == 0:

            return "explodiu", matriz
        
        return None, matriz


    #matriz cliente
    def gera_campo_minado(x_ref, y_ref, tela, matriz_binaria, aresta, lotes): 

        for i in range(0, len(matriz_binaria)):

            matriz_linha = matriz_binaria[i]

            x_ref = aresta

            for j in range(0, len(matriz_linha)):

                novo_lote = Quadrado(aresta)

                if matriz_linha[j] != 2:

                    novo_lote.altera_cor(r=200, g=200, b=200)
                
                else:
                    novo_lote.altera_cor(r=50, g=50, b=50)

                # Define onde os quadrados vão aparecer na tela
                # o blit desenha eles na superficie onde o jogo roda to draw them on the screen surface
                tela.blit(novo_lote.surf, (x_ref, y_ref))

                x_ref += aresta + 1
            
            y_ref += aresta + 1

        

        
    


    # print('_ _ _ _ _ _ _ _ \n')

    # for i in range(0, 5):

    #     print('| ', end=' ')

    #     matriz_c = matriz_r[i]

    #     for j in range(0, 5):

    #         print(matriz_c[j], end=' ')
        
    #     print(' |')

    #     matriz_r.append(matriz_c)

    # print('_ _ _ _ _ _ _ _ \n')
