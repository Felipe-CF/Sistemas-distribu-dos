import re, socket, time, json
from matriz import Matriz

MEU_IP = '127.0.0.1'

MINHA_PORTA = 8000

tcp_receber = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

udp_envio = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


MEU_SERVIDOR = (MEU_IP, MINHA_PORTA) # Definir o IP e porta para o servidor ouvir

tcp_receber.bind(MEU_SERVIDOR)  # Faz o bind do IP e da porta para começar a ouvir


tcp_receber.listen(1)   # Começar a ouvir (aguardar conexão)

print(f"| -----  Esperando os jogadores aqui {MEU_IP}:{MINHA_PORTA}...   ----- |")


conexao_jogador, add_jogador = tcp_receber.accept() # Aceitar conexão do cliente

nova_mensagem = conexao_jogador.recv(1024) # espera a 1° conexão

print(f"O jogador {add_jogador} foi encontrado")

jogador = {
    'conexao_jogador': conexao_jogador, # conexão para validar a vez do jogador
    'endereco': add_jogador # endereço para a comunicação UDP
}

time.sleep(2) # espera para sincronizar a resposta

conexao_jogador.sendall(f"{add_jogador[1]+1}".encode('utf-8')) # resposta da 1° conexão

print(add_jogador[1]+1)


tcp_receber.close()
