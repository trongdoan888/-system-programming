import socket

HOST = "127.0.0.1"
PORT = 5001

client_socket = socket.socket()
client_socket.connect((HOST, PORT))

message = input("Nhập tin nhắn: ")
while message.lower() != 'q':
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print('Phản hồi từ server: ', data)
    message = input("Nhập tin nhắn: ")


client_socket.close()