import socket, pygame, time, json
from pygame.locals import *
from matriz import Matriz

ip_jogo = input("Digite o endereço IP do servidor do jogo: ")

porta_jogo = int(input("Digite a porta do servidor do jogo: "))

tcp_envio = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar o socket TCP

tcp_envio.settimeout(10)  # Definir timeout de 10 segundos

udp_receber = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criar o socket UDP

udp_receber.bind(('127.0.0.1', 8001)) 

# Conectar ao servidor TCP
try:
    DESTINO = (ip_jogo, porta_jogo)

    tcp_envio.connect(DESTINO)

    tcp_envio.sendall("jogo".encode('utf-8'))

    print(f"Conectado ao servidor {ip_jogo}:{porta_jogo}.")

except socket.error as e:

    print(f"Erro ao conectar ao servidor: {e}")

    exit()

jogo = True

matriz = ""

jogando = False

# Loop principal para enviar mensagens
while True:

    dados, origem = udp_receber.recvfrom(1024)  # fica ouvindo o servidor do jogo

    endereco_mensagem = origem[0] # pego o endereço da mensagem

    ip_mensagem = origem[1] # pego a porta

    if jogando and endereco_mensagem == ip_jogo and ip_mensagem == ip_jogo and matriz:

        matriz = json.loads(dados.decode('utf-8'))

        if ("Escolha outro Lote" or "pontuação") in matriz:
            pygame.init()
            
            tela = pygame.display.set_mode((800, 800)) # display do jogo

            lotes = pygame.sprite.Group()

            Matriz.gera_campo_minado(
                x_ref=50, y_ref=50, 
                tela=tela, 
                matriz_binaria=matriz, 
                aresta=100, lotes=lotes
                )

            linha = input("Escolha a linha do lote: ")

            coluna = input("Escolha a coluna do lote:: ")

            tcp_envio.send(bytes(f"linha {linha} e coluna {coluna}", "utf-8"))

            print("Jogada enviada")

            lotes.draw(tela)

            pygame.display.flip()

            pygame.quit()

        elif 'Parabéns' in matriz:
            print("Você ganhou.")

            break
        
        else:
            print("Você perdeu.")

            break

            

print("O jogo acabou.")

# encerra a conexão
tcp_envio.close()

# print("Conexão encerrada.")