from socket import *
import sys

host = 'localhost'
port = 7777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

data = input('Отправить серверу: ')
if not data : 
    tcp_socket.close() 
    sys.exit(1)

#encode -  decode 
data = str.encode(data)
tcp_socket.send(data)
data = bytes.decode(data)
data = tcp_socket.recv(1024)
print("Ответ сервера: " + bytes.decode(data,"utf-8"))

tcp_socket.close()
