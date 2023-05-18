import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9998
server.connect((host, port))


def sender():
    global server
    while True:
        msg = input(">>")
        if len(msg) > 0:
            server.send(bytes(msg, "utf-8"))


def recv():
    while True:
        print(server.recv(10255).decode("utf-8"))


def main():
    t = threading.Thread(target=recv)
    t.daemon = True
    t.start()
    sender()


main()
