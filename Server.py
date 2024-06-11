import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 2021))
server.listen()

# Получение локального IP-адреса сервера
local_ip = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
print(f"Сервер запущен на локальном IP-адресе: {local_ip}")

while True:
    client, address = server.accept()
    print(f"Новое подключение от {address}")

    # Отправка сообщения "готов к работе" клиенту
    client.send("Готов к работе".encode("utf-8"))

    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Получено сообщение: {data.decode()}")