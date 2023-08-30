import socket
import threading

# Pegando o ip e o protocolo TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define qual o endereço e a porta que o servidor recebe as requisições
server.bind(('127.0.0.1', 5555))
# Liga o servidor
server.listen()

clients = []

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)
        if not message:
            break
        for client in clients:
            if client != client_socket:
                client.send(message.encode('utf-8'))

while True:
    client_socket, _ = server.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
