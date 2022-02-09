from socketserver import *

#данные сервера
host = '0.0.0.0'#'localhost'
port = 7777
addr = (host,port)

#Наследуем свой обработчик запросов от TCP подкласса StreamRequestHandler
class MyTCPHandler(StreamRequestHandler):
    
    #Обработаем запрос. 
    def handle(self):     
        self.data = self.request.recv(1024)
        print ("Клиент отправил: " + bytes.decode( (self.data))) 
        print('адрес клиента:' + str(self.client_address))
          
        self.request.sendall('Сервер отправил ответ. Всем привет!'.encode("utf-8"))  #'raw_unicode_escape'))

if __name__ == "__main__":
    #Создаем экземпляр класса TCPServer
    server = TCPServer(addr, MyTCPHandler)
  
    print('Cтартуем сервер...')
    server.serve_forever() #serve_forever - сервер работает постоянно
