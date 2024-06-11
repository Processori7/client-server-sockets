import socket
import webbrowser
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 2021))
server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)

        # Команды
        if data =="сайт":
            webbrowser.open("https://it-mir.info/")
