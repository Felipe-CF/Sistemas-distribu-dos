import socket, json


UDP_IP = "127.0.0.1"

UDP_PORT = 8000

teste = []
MESSAGE = json.dumps(teste).encode('utf-8')

print("Servidor-UDP  IP: %s" % UDP_IP)

print("Servidor-UDP porta: %s" % UDP_PORT) 

print("Mensagem: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

