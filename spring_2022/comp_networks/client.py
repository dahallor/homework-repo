import socket
import pdb
from auth import *

#Add functionality for DMing or main chat room. delimit it by backslash. Look up how to make seperate chat rooms

HEADER = 64
BODY = 4096
PORT = 1719
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT = "EXIT" #look at DFA
DELIMIT = b'\n'
END = b'\n\n'

def _assemble_session_header(USERNAME, code):
    head = code.encode(FORMAT)
    head += ";".encode(FORMAT)
    head += USERNAME.encode(FORMAT)
    head += "\n".encode(FORMAT)
    return head

def _assemble_header_encode(USERNAME, version, code):
    head = version.encode(FORMAT)
    head += ";".encode(FORMAT)
    head += code.encode(FORMAT)
    head += ";".encode(FORMAT)
    head += USERNAME.encode(FORMAT)
    head += "\n".encode(FORMAT)
    return head
'''
def _assemble_header_len(USERNAME, version, code):
    head_len = str(len(version)).encode(FORMAT)
    head_len += str(";").encode(FORMAT)
    head_len += str(len(code)).encode(FORMAT)
    head_len += str(";").encode(FORMAT)
    head_len += str(len(USERNAME)).encode(FORMAT)
    head_len += str("\n").encode(FORMAT)
    return head_len
    '''

def send_nonsession_header(USERNAME, version, code):
    head = _assemble_header_encode(USERNAME, version, code)
    head_len = str(head)
    #pdb.set_trace()
    head_len = b' ' * (HEADER - len(head_len))
    client.send(head_len)
    client.send(head)

def send_session_header(USERNAME, code):
    head = _assemble_session_header(USERNAME, code)
    head_len = str(head)
    head_len = b' ' * (HEADER - len(head_len))
    pdb.set_trace()
    client.send(head_len)
    client.send(head)

def send_body(msg):
    msg += "\n\n"
    message = msg.encode(FORMAT)
    body_len = str(len(message)).encode(FORMAT)
    body_len = b' ' * (BODY - len(body_len))
    client.send(body_len)
    client.send(message)


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    auth = Auth()
    USERNAME = auth.authenticate()
    version = "1.0"
    code = "10"
    send_nonsession_header(USERNAME, version, code)
    while True:
        msg = input()
        send_session_header(USERNAME, code)
        send_body(msg)
