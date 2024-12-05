import socket, pygame, time
from pygame.locals import *
from matriz import Matriz

ip_jogo = input("Digite o endereço IP do servidor do jogo: ")
porta_jogo = int(input("Digite a porta do servidor do jogo: "))

# Criar o socket TCP
tcp_envio = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_envio.settimeout(10)  # Definir timeout de 10 segundos

# Criar o socket UDP
udp_receber = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_receber.bind(('127.0.0.1', 8001))

# Conectar ao servidor TCP
try:
    DESTINO = (ip_jogo, porta_jogo)
    tcp_envio.connect(DESTINO)
    print(f"Conectado ao servidor {ip_jogo}:{porta_jogo}.")
except socket.error as e:
    print(f"Erro ao conectar ao servidor: {e}")
    exit()



print(f"Conectado ao servidor do jogo = {ip_jogo}:{porta_jogo}.")

# crio o servidor UDP que ficará responsavel por receber a matriz para gerar o campo minado

udp_receber.bind((ip_jogador, porta_jogador))


jogo = True

matriz = ""

jogando = False

# Loop principal para enviar mensagens
while True:

    # fica ouvindo o servidor do jogo
    dados, origem = udp_receber.recvfrom(1024) 

    endereco_mensagem = origem[0] # pego o endereço da mensagem

    ip_mensagem = origem[1] # pego a porta

    if endereco_mensagem == ip_jogo and ip_mensagem == ip_jogo and matriz:

        matriz = dados.decode('utf-8')

        # se o jogo ainda não começou
        if not jogando:

            print("Se quiser jogar digite '1', ou '2' para encerrar.")

            mensagem = input("Digite sua mensagem: ")

            if mensagem == '2':

                print("Desconectando...")

                break
            
            elif mensagem == '1':

                tcp_envio.send(bytes(mensagem, "utf8"))

                jogando = True

        # se o jogo já começou
        else:

            if matriz == "Escolha outro Lote" or "pontuação" in matriz:
                pygame.init()

                # display do jogo
                tela = pygame.display.set_mode((800, 800))

                lotes = pygame.sprite.Group()
                
                # variavel que mantem o jogo rodando
                gameOn = True

                # loop que mantem o jogo
                while gameOn:

                    Matriz.gera_campo_minado(x_ref=50, y_ref=50, tela=tela, matriz_binaria=matriz, aresta=100, lotes=lotes)

                    print("Escolha as posições do lote ")
                    linha = input("linha: ")
                    coluna = input("coluna: ")
                    print("Jogada enviada")

                    # # checa se, por exemplo, a janela foi fechada 
                    # if pygame.event.get().type == QUIT:
                    gameOn = False

                    lotes.draw(tela)

                    pygame.display.flip()

                    pygame.quit()

            else:
                print(matriz)

                break
            

print("O jogo acabou.")

# encerra a conexão
tcp_envio.close()

print("Conexão encerrada.")