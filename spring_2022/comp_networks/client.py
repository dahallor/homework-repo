import socket
from auth import *

HEADER = 64
PORT = 40000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT = "EXIT" #look at DFA

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(username, msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(username, message)

if __name__ == '__main__':
    auth = Auth()
    username = auth.authenticate()
    while True:
        msg = input()
        send(username, msg)
        #send(DISCONNECT)