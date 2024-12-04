#!/usr/bin/python3
import socket

ip_jogo = input("Digite o endereço IP do servidor do jogo: ")

porta_jogo = int(input("Digite a porta do servidor do jogo: "))

tcp_envio = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Criar o socket TCP

tcp_envio.settimeout(10)   # Definir timeout de 10 segundos

DESTINO = (ip_jogo, porta_jogo) # Destino da conexão (IP + Porta)

try:
    # Conectar ao servidor
    tcp_envio.connect(DESTINO)

except socket.error as e:
    print(f"Erro ao conectar ou enviar dados: {e}")


print(f"Conectado ao servidor do jogo = {ip_jogo}:{porta_jogo}.")


# crio o servidor UDP que ficará responsavel por receber a matriz para gerar o campo minado
ip_jogador = input("Digite o seu endereço IP para jogar: ")

porta_jogador = int(input("Digite a sua porta para jogar: "))

udp_receber = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

udp_receber.bind((ip_jogador, porta_jogador))


jogo = True

matriz = ""

cadastrado = False


# Loop principal para enviar mensagens
while True:

    # fica ouvindo o servidor do jogo
    dados, origem = udp_receber.recvfrom(1024) 

    endereco_mensagem = origem[0] # pego o endereço da mensagem

    ip_mensagem = origem[1] # pego a porta

    if endereco_mensagem == ip_jogo and ip_mensagem == ip_jogo and matriz:

        matriz = dados.decode('utf-8')

    if not cadastrado:

        if matriz == 'Você é um jogador': # o jogador já foi cadastrado
            cadastrado = True

            continue # volta a ouvir as mensagme do servidor do jogo

        print("Se quiser jogar digite '1', ou '2' para encerrar.")

        mensagem = input("Digite sua mensagem: ")

        if mensagem == '2':

            print("Desconectando...")

            break
        
        elif mensagem == '1':

            tcp_envio.send(bytes(mensagem, "utf8"))

            cadastrado = True

        else:
            continue

    # valida se a mensagem veio do servidor do jogo
    elif endereco_mensagem == ip_jogo and ip_mensagem == ip_jogo:

        matriz = dados.decode('utf-8')

        if matriz == "Sua vez! Informe qual lote voce deseja capinar!":
            jogo = False


# encerra a conexão
tcp_envio.close()

print("Conexão encerrada.")