# Lote Premiado

## Quantidade de bombas por partida -  5

## Cores dos Lotes

|         Cor              |      valor            | RGB            |
|--------------------------|-----------------------|----------------|
| Amarelo Ouro             |       4               | (255, 215, 0)  |
| Prata                    |       2               | (192, 192, 192)|
| Verde Grama Após a Chuva |       1               | (34, 139, 34)  |
| Marrom Cor de Terra Suja |       3               | (139, 69, 19)  |



## Comunicação TCP - exemplo

|                          |      Servidor         |                |
|--------------------------|-----------------------|----------------|
    import socket
    from matriz import Matriz

    MINHA_PORTA = 8000

    MEU_IP = '127.0.0.1'


    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Definir o IP e porta para o servidor ouvir
    MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)

    tcp.bind(MEU_SERVIDOR)  # Faz o bind do IP e da porta para começar a ouvir

    tcp.listen(1)  # Começar a ouvir (aguardar conexão)

    print(f"Servidor ouvindo na porta {MINHA_PORTA}...")

    # Aceitar conexão do cliente
    conexao, docliente = tcp.accept()
    print("O cliente =", docliente, "se conectou")

    teste = True

    # Loop para receber mensagens do cliente
    while teste:
        Mensagem_Recebida = conexao.recv(1024)

        if Mensagem_Recebida:
            # Se houver uma nova mensagem, imprime na tela
            print("Recebi =", Mensagem_Recebida.decode("utf8"), ", Do cliente", docliente)
            teste = False

    # Fechar a conexão ao terminar
    conexao.close()


|                          |      Cliente         |                |
|--------------------------|-----------------------|----------------|
    #!/usr/bin/python3
    import socket

    # Solicitar IP e porta do servidor ao usuário

    IP_Servidor = input("Digite o endereço IP do servidor: ")
    PORTA_Servidor = int(input("Digite a porta do servidor: "))

    # Criar o socket TCP
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.settimeout(10)  # Definir timeout de 10 segundos

    Destino da conexão (IP + Porta)
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



## Comunicação UDP - exemplo

|          Servidor        |||
|--------------------------|-----------------------|----------------|
   1 import socket
   2 
   3 UDP_IP = "127.0.0.1"
   4 UDP_PORT = 5005
   5 
   6 sock = socket.socket(socket.AF_INET, # Internet
   7                      socket.SOCK_DGRAM) # UDP
   8 sock.bind((UDP_IP, UDP_PORT))
   9 
  10 while True:
  11     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  12     print("received message: %s" % data)


|          Cliente        |||
|--------------------------|-----------------------|----------------|
   1 import socket
   2 
   3 UDP_IP = "127.0.0.1"
   4 UDP_PORT = 5005
   5 MESSAGE = b"Hello, World!"
   6 
   7 print("UDP target IP: %s" % UDP_IP)
   8 print("UDP target port: %s" % UDP_PORT)
   9 print("message: %s" % MESSAGE)
  10 
  11 sock = socket.socket(socket.AF_INET, # Internet
  12                      socket.SOCK_DGRAM) # UDP
  13 sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))