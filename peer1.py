import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
server.bind((host, port))
server.listen(3)

connections = []
address = []


def connectionAcp():
    global server
    while True:
        conn, add = server.accept()
        connections.append(conn)
        address.append(add)
        print(f"New connection from {add[0] + add[1]}")

def handle(c):
    while True:
        msg=input()
        if len(msg)>0:
            try:
                c.send(bytes(msg, 'utf-8'))
            except Exception as error:
                print(f"Unable to send message due to: {Exception}")
        if msg == "back":
            break
            main()

def recv():
    while True:
        for nn, x in enumerate(connections):
            try:
                print(x.recv(1024).decode("utf-8"))
            except:
                del connections[nn]
                del address[nn]



def connectionList():
    global connections
    result = ""
    for i, cc in enumerate(connections):
        try:
            cc.send(bytes("checked by peer", "utf-8"))
            result=address[i][len(address)-1]+':'+str(address[len(address)]+'\n')
        except:
            pass

    return result


def main():
    t1 = threading.Thread(target=connectionAcp)
    t1.daemon = True

    t2 = threading.Thread(target=recv)

    t1.start()
    t2.start()

    while True:
        cmd = input(">")
        if cmd == "list":
            print(connectionList())
        if cmd[:7] == "select":
            handle(connections[int(cmd[8:])])


main()
