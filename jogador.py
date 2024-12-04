#!/usr/bin/python3
import socket

ip_jogo = input("Digite o endereço IP do servidor do jogo: ")
porta_jogo = int(input("Digite a porta do servidor do jogo: "))

# Criar o socket TCP
tcp_envio = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir timeout de 10 segundos
tcp_envio.settimeout(10)  

# Destino da conexão (IP + Porta)
DESTINO = (ip_jogo, porta_jogo)

try:
    # Conectar ao servidor
    tcp_envio.connect(DESTINO)

except socket.error as e:
    print(f"Erro ao conectar ou enviar dados: {e}")
    

print(f"Conectado ao servidor do jogo = {IP_Servidor}:{PORTA_Servidor}.")

print("Se quiser jogar digite '1', ou '2' para encerrar.")

# Loop principal para enviar mensagens

while True:

    mensagem = input("Digite sua mensagem: ")

    if mensagem == '2':

        print("Desconectando...")

        break
    
    if mensagem == '1':
        tcp_envio.send(bytes(mensagem, "utf8"))

if mensagem == '1':

    # jogo começa

    udp_receber = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    endereco = '127.0.0.1'

    porta = 8001

    jogo = True

    sock.bind((endereco, porta))

    while jogo:

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes





# encerra a conexão
tcp.close()

print("Conexão encerrada.")