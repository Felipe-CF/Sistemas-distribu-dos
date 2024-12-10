import socket, pygame, time, json
from pygame.locals import *
from matriz import Matriz

PORTA_JOGO = 8001

ip_servidor = input("Digite o endereço IP do servidor do jogo: ")

porta_servidor = int(input("Digite a porta do servidor do jogo: "))

tcp_conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar o socket TCP

tcp_conexao.settimeout(10)  # Definir timeout de 10 segundos



# Conectar ao servidor TCP
try: 
    DESTINO = (ip_servidor, porta_servidor)

    tcp_conexao.connect(DESTINO)

    tcp_conexao.sendall("jogo".encode('utf-8'))

    print(f"Conectado ao servidor {ip_servidor}:{porta_servidor}.")

    print(f"Esperando a porta para receber a matriz.")

    while True:

        dados_servidor = tcp_conexao.recv(1024)  # fica ouvindo o servidor do jogo

        origem = tcp_conexao.getpeername() # pega o IP e a porta de origem da mensagem

        ip_mensagem = origem[0] # pego a porta

        endereco_mensagem = origem[1] # pego o endereço da mensagem

        if (ip_mensagem == ip_servidor and endereco_mensagem == porta_servidor):

            PORTA_JOGO = int(dados_servidor.decode('utf-8')) # pego a porta enviada pelo servidor
            
            break
    
except socket.error as e:

    print(f"Erro ao conectar ao servidor: {e}")

    exit()

print(f"porta recebida.")

udp_conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criar o socket UDP

udp_conexao.bind(('127.0.0.1', PORTA_JOGO)) 

udp_conexao.settimeout(10)

matriz = ""

time.sleep(2)

tcp_conexao.sendall("continue".encode('utf-8'))

while True: # Loop principal para enviar mensagens

    dados_servidor, origem = udp_conexao.recvfrom(1024)  # fica ouvindo o servidor do jogo

    endereco_mensagem = origem[0] # pego o endereço da mensagem

    ip_mensagem = origem[1] # pego a porta 

    if ip_mensagem == ip_servidor and endereco_mensagem == porta_servidor:
    
        matriz = json.loads(dados_servidor.decode('utf-8'))
        
        print(matriz['mensagem'])

        if ("escolha o lote" or "pontuação" or "escolha outro lote") in matriz['mensagem']:

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

            tcp_conexao.send(bytes(f"linha {linha} e coluna {coluna}", "utf-8"))

            print("Jogada enviada")

            lotes.draw(tela)

            pygame.display.flip()

            pygame.quit()

        elif 'parabéns' in matriz:

            print("Você ganhou.")

            break
        
        else:
            print("Você perdeu.")

            break

            

print("O jogo acabou.")

# encerra a conexão
tcp_conexao.close()

# print("Conexão encerrada.")