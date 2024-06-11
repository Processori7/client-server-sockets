import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.11', 2021))

while True:
    client.send((input().encode("utf-8")))
