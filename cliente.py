#!/usr/bin/python3
import socket

# Solicitar IP e porta do servidor ao usuário
IP_Servidor = input("Digite o endereço IP do servidor: ")
PORTA_Servidor = int(input("Digite a porta do servidor: "))

# Criar o socket TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.settimeout(10)  # Definir timeout de 10 segundos

# Destino da conexão (IP + Porta)
DESTINO = (IP_Servidor, PORTA_Servidor)

try:
    # Conectar ao servidor
    tcp.connect(DESTINO)
    print(f"Conectado ao servidor {IP_Servidor}:{PORTA_Servidor}.")
    print("Você pode começar a enviar mensagens (digite 'sair' para desconectar).")

    # Loop principal para enviar mensagens
    while True:
        Mensagem = input("Digite sua mensagem: ")
        if Mensagem.lower() == 'sair':
            print("Desconectando...")
            break
        tcp.send(bytes(Mensagem, "utf8"))
except socket.error as e:
    print(f"Erro ao conectar ou enviar dados: {e}")
finally:
    tcp.close()
    print("Conexão encerrada.")