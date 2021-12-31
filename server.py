import socket

from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",5555))

server.listen(1000)

all_clients = {}
def client_thread(client):
    while True:
        try:
         msg = client.recv(1024)
         print(msg)
         for c in all_clients:
             c.send(msg)
        
        except:
            del all_clients[client]
            client.close()
            break




while True:
    print("Waiting for connection")
    client, address = server.accept()
    print("Connection established")
    name = client.recv(1024).decode()
   
    print(name)

    all_clients[client] = name
    
    thread = Thread(target = client_thread,args=(client, ))
    thread.start()


