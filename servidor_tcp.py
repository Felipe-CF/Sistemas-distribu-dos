import re
import socket
from matriz import Matriz

MINHA_PORTA = 8000

MEU_IP = '127.0.0.1'

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir o IP e porta para o servidor ouvir
MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)

# Faz o bind do IP e da porta para começar a ouvir
tcp.bind(MEU_SERVIDOR)  

# Começar a ouvir (aguardar conexão)
tcp.listen(1)  

print(f"Jogo rodando aqui {MEU_IP}:{MINHA_PORTA}...")

# Aceitar conexão do cliente
conexao, add_cliente = tcp.accept()

matriz_de_lotes = Matriz.gera_matriz()

vencedor = False

print("| -----  Lote Premiado começou!   ----- |")

# Enquanto não houver um vencedor

total_jogadores = 0

jogadores = []

enderecos = []

jogador_da_vez = 0

while not vencedor:
    
    nova_mensagem = conexao.recv(1024)

    if total_jogadores < 2 and nova_mensagem:

        mensagem = nova_mensagem.decode('utf8')

        if 'Quero jogar' in mensagem:

            total_jogadores += 1

            jogadores.append(conexao)

            enderecos.append(add_cliente)

                
    # se já tiver achado os 2 jogadores e mensagem foi enviado de um dos 2...
    elif conexao in jogadores and jogador_da_vez == jogadores.index(conexao):

        regex_msg = re.search(r'linha=(?P<l>.?)\s*coluna=(?P<c>.?)', mensagem)

        linha = regex_msg.group('l')

        coluna = regex_msg.group('c')

        atualizacao, matriz_de_lotes = Matriz.atualiza_matriz(int(linha), int(coluna), matriz_de_lotes)

        if 'explodiu' in atualizacao:
            pass

    
    else:
        pass
            





            



# Fechar a conexão ao terminar
conexao.close()