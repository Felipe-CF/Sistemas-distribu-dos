import random

def matriz(): 
    matriz_r = []

    for i in range(0, 5):

        matriz_c = []

        for j in range(0, 5):

            matriz_c.append(random.randint(0, 1))
        
        matriz_r.append(matriz_c)
    
    return matriz_r

    # print('_ _ _ _ _ _ _ _ \n')

    # for i in range(0, 5):

    #     print('| ', end=' ')

    #     matriz_c = matriz_r[i]

    #     for j in range(0, 5):

    #         print(matriz_c[j], end=' ')
        
    #     print(' |')

    #     matriz_r.append(matriz_c)

    # print('_ _ _ _ _ _ _ _ \n')
