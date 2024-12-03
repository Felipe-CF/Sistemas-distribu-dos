import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))

while True:

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    print("Mensagem recebida: %s" % data)
    print("Cliente: IP = {} Porta = {}".format(addr[0], addr[1]))