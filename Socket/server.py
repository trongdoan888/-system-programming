import socket

HOST = '127.0.0.1'

PORT = 5001

server = socket.socket()
server.bind((HOST, PORT))
server.listen()
print(f"Server đang lắng nghe trên {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"Kết nối từ: {addr}")
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Dữ liệu nhận từ clinet: {data}")

    response = data.upper()
    conn.send(response.encode())

conn.close()