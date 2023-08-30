import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

def receive_messages():
    print("Connected!")
    while True:
        message = client.recv(1024).decode('utf-8')
        print(message)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    client.send(message.encode('utf-8'))
