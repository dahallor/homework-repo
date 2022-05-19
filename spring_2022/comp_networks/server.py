import socket
import threading

HEADER = 64
PORT = 40000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT = "EXIT" #look at DFA

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def client_handler(username, connection, address):
    print(f"{address} connected")
    connected = True
    while connected:
        try:
            msg_len = connection.recv(HEADER).decode(FORMAT)
            msg_len = int(msg_len)
            msg = connection.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT:
                connected = False
            print(f"{username} {msg}")
        except:
            pass
    connection.close()

def start_server():
    server.listen()
    print(f"[LISTENING] on {SERVER}")
    while True:
        username, connection, address = server.accept()
        thread = threading.Thread(target = client_handler, args = (username, connection, address))
        thread.start()
        print(f"num connections: {threading.active_count() -1}")


if __name__ == '__main__':
    print("[START SERVER]")
    start_server()