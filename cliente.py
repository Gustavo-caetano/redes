
import socket

host = '127.0.0.1'
porta = 22205

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, porta))

print('Informações da máquina do servidor:\n',s.recv(1024).decode())

while True:
    dado = input()
    s.send(str.encode(dado))
    data = s.recv(1024)
    if(dado == '0'):
        break
    print(data.decode())


s.close()