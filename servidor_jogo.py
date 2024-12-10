import re, socket, time, json
from matriz import Matriz

MEU_IP = '127.0.0.1'
# MEU_IP = '25.49.249.117'

MINHA_PORTA = 8000

tcp_receber = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

udp_envio = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


MEU_SERVIDOR = (MEU_IP, MINHA_PORTA) # Definir o IP e porta para o servidor ouvir

tcp_receber.bind(MEU_SERVIDOR)  # Faz o bind do IP e da porta para começar a ouvir


tcp_receber.listen(1)   # Começar a ouvir (aguardar conexão)

print(f"| -----  Esperando os jogadores aqui {MEU_IP}:{MINHA_PORTA}...   ----- |")


conexao_jogador, add_jogador = tcp_receber.accept() # Aceitar conexão do cliente

nova_mensagem = conexao_jogador.recv(1024) # espera a 1° conexão

if conexao_jogador:

    print(f"O jogador {add_jogador} foi encontrado")
    
    jogador = {
        'conexao_jogador': conexao_jogador, # conexão para validar a vez do jogador
        'endereco': add_jogador # endereço para a comunicação UDP
    }

    time.sleep(2)
    
    conexao_jogador.sendall(f"{add_jogador[1]+1}".encode('utf-8')) 

    print(add_jogador[1]+1)

    confirmacao = conexao_jogador.recv(1024) # espera a confirmação

    # cria a matriz do jogo 5x5 (em teste)
    matriz_de_lotes = Matriz.gera_matriz()

    fim_de_jogo = False

    pontos = 0

    # servidor TCP que mantém o jogo rodando
    while not fim_de_jogo:

        time.sleep(2)

        dados = {
            'mensagem': 'Escolha o lote voce deseja capinar!',
            'matriz': matriz_de_lotes
        }
        
        dados_serial = json.dumps(dados)

        udp_envio.sendto(dados_serial.encode('utf-8'), jogador['endereco'])

        resposta_jogador = conexao_jogador.recv(1024)

        if resposta_jogador and conexao_jogador == jogador['conexao']:

            mensagem = resposta_jogador.decode('utf-8')

            regex_msg = re.search(r'linha=(?P<l>.?)\s*e\s*coluna=(?P<c>.*)', mensagem)

            linha = int(regex_msg.group('l'))

            coluna = int(regex_msg.group('c'))

            atualizacao, matriz_de_lotes = Matriz.atualiza_matriz(linha, coluna, matriz_de_lotes)

            if atualizacao == 'explodiu':
                
                udp_envio.sendto("Você explodiu!".encode('utf-8'), jogador['endereco'])

                fim_de_jogo = True

            elif atualizacao == 'escolhido':
                udp_envio.sendto("escolha outro lote".encode('utf-8'), jogador['endereco'])

            else:
                matriz_de_lotes[linha][coluna] = 2

                pontos += 1

                if pontos < 20:
                    udp_envio.sendto(f"sua pontuação é {pontos} Escolha outro lote".encode('utf-8'), jogador['endereco'])
                
                else:
                    udp_envio.sendto(f"parabéns!".encode('utf-8'), jogador['endereco'])


    print("| -----  Lote Premiado terminou!   ----- |")

    time.sleep(5)

    # Fechar a conexão ao terminar
    conexao_jogador.close()


    # else:
    #     # udp_envio.sendto("inscrição inválida".encode('utf-8'), add_jogador)

