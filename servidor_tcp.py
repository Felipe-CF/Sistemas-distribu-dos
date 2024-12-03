import socket
from matriz import Matriz

MINHA_PORTA = 8000

MEU_IP = '127.0.0.1'


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir o IP e porta para o servidor ouvir
MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)

tcp.bind(MEU_SERVIDOR)  # Faz o bind do IP e da porta para começar a ouvir

tcp.listen(1)  # Começar a ouvir (aguardar conexão)

# print(f"Servidor ouvindo na porta {MINHA_PORTA}...")

# Aceitar conexão do cliente
conexao, docliente = tcp.accept()

# print("O cliente =", docliente, "se conectou")

matriz_de_lotes = Matriz.maatriz()

teste = True

print("| -----  Lote Premiado começou!   ----- |")
# Loop para receber mensagens do cliente
while teste:
    
    Mensagem_Recebida = conexao.recv(1024)

    if Mensagem_Recebida:

        mensagem = Mensagem_Recebida.decode('utf8')

        if mensagem == 'matriz':
        # Se houver uma nova mensagem, imprime na tela
            print("Recebi =", Mensagem_Recebida.decode("utf8"), ", Do cliente", docliente)
            teste = False

# Fechar a conexão ao terminar
conexao.close()