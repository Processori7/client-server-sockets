import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.3', 2021))

# Получение ответа от сервера
response = client.recv(1024)
print(f"Сервер ответил: {response.decode()}")

while True:
    client.send((input().encode("utf-8")))