import re
import socket
from matriz import Matriz

MINHA_PORTA = 8000

MEU_IP = '127.0.0.1'

tcp_receber = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

udp_envio = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Definir o IP e porta para o servidor ouvir
MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)

# Faz o bind do IP e da porta para começar a ouvir
tcp_receber.bind(MEU_SERVIDOR)  

# Começar a ouvir (aguardar conexão)
tcp_receber.listen(1)  

print(f"| -----  Esperando os jogadores aqui {MEU_IP}:{MINHA_PORTA}...   ----- |")

# Aceitar conexão do cliente
conexao, add_cliente = tcp_receber.accept()

total_jogadores = 0

jogadores = []

while total_jogadores < 2:

    nova_mensagem = conexao.recv(1024)

    mensagem = nova_mensagem.decode('utf8')
    
    if 'Quero jogar' in mensagem:

            total_jogadores += 1

            # a resposta será via UDP, por isso não precisamos salvar a conexão
            # somente o endereço
            jogadores.append(add_cliente)

            print(f"O jogador {add_cliente} foi cadastrado")

    else:
        udp_envio.sendto("inscrição inválida".encode('utf-8'), add_cliente)


# cria a matriz do jogo 5x5 (em teste)
matriz_de_lotes = Matriz.gera_matriz()

jogador_da_vez = jogadores[0]

vencedor = False

print("| -----  Lote Premiado começou!   ----- |")

# Enquanto não houver um vencedor
while not vencedor:
    
    udp_envio.sendto("Sua vez! Informe qual lote voce deseja capinar! ".encode('utf-8'), jogador_da_vez)

    resposta_jogador = conexao.recv(1024)

    if resposta_jogador:

        mensagem = resposta_jogador.decode('utf-8')

        regex_msg = re.search(r'linha=(?P<l>.?)\s*coluna=(?P<c>.*)', mensagem)

        linha = int(regex_msg.group('l'))

        coluna = int(regex_msg.group('c'))

        atualizacao, matriz_de_lotes = Matriz.atualiza_matriz(linha, coluna, matriz_de_lotes)

        # se o jogo terminou...
        if atualizacao == 'explodiu':
            
            # organizo as mensagens para os respectivos jogadores...
            if conexao is not jogadores[0]:
                fim_de_jogo = ['Voce ganhou :) ', 'Você perdeu :(']
            
            else:
                fim_de_jogo = ['Você perdeu :(', 'Voce ganhou :) ']

            # depois envio uma-a-uma
            for i in range(0, 2):
                udp_envio.sendto(fim_de_jogo[i].encode('utf-8'), jogadores[i])

        elif atualizacao == 'escolhido':
            udp_envio.sendto("Escolha outro lote".encode('utf-8'), conexao)

        else:
            matriz_de_lotes[linha][coluna] = 2

            if jogador_da_vez == jogadores[0]:
                jogador_da_vez = jogadores[1]
            
            else:
                jogador_da_vez = jogadores[0]

    else:
        pass
            





            



# Fechar a conexão ao terminar
conexao.close()