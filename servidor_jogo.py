import re, socket, time
from matriz import Matriz

MEU_IP = '127.0.0.1'

MINHA_PORTA = 8000

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


# servidor TCP espera os jogadores serem achados
while True:

    nova_mensagem = conexao.recv(1024)

    mensagem = nova_mensagem.decode('utf8')
    
    if 'quero jogar' in mensagem:

        print(f"O jogador {add_cliente} foi encontrado")

        jogador = {
            'conexao': conexao, # conexão para validar a vez do jogador
            'endereco': add_cliente # endereço para a comunicação UDP
        }
        
        udp_envio.sendto("Você é um jogador".encode('utf-8'), jogador['endereco'])

        break

    else:
        udp_envio.sendto("inscrição inválida".encode('utf-8'), add_cliente)

# cria a matriz do jogo 5x5 (em teste)
matriz_de_lotes = Matriz.gera_matriz()

fim_de_jogo = False

pontos = 0

print("| -----  Lote Premiado começou!   ----- |")

# servidor TCP que mantém o jogo rodando
while not fim_de_jogo:
    
    udp_envio.sendto(matriz_de_lotes.encode('utf-8'), jogador['endereco'])

    udp_envio.sendto("Informe qual lote voce deseja capinar!".encode('utf-8'), jogador['endereco'])

    resposta_jogador = conexao.recv(1024)

    if resposta_jogador and conexao == jogador['conexao']:

        mensagem = resposta_jogador.decode('utf-8')

        regex_msg = re.search(r'linha=(?P<l>.?)\s*coluna=(?P<c>.*)', mensagem)

        linha = int(regex_msg.group('l'))

        coluna = int(regex_msg.group('c'))

        atualizacao, matriz_de_lotes = Matriz.atualiza_matriz(linha, coluna, matriz_de_lotes)

        if atualizacao == 'explodiu':
            
            udp_envio.sendto("Você explodiu!".encode('utf-8'), jogador['endereco'])

            fim_de_jogo = True


        elif atualizacao == 'escolhido':
            udp_envio.sendto("Escolha outro lote".encode('utf-8'), jogador['endereco'])

        else:
            matriz_de_lotes[linha][coluna] = 2

            pontos += 1

            if pontos < 20:
                udp_envio.sendto(f"Sua pontuação é {pontos} Escolha outro lote".encode('utf-8'), jogador['endereco'])
            
            else:
                udp_envio.sendto(f"Parabéns!".encode('utf-8'), jogador['endereco'])



print("| -----  Lote Premiado terminou!   ----- |")

time.sleep(5)

# Fechar a conexão ao terminar
conexao.close()