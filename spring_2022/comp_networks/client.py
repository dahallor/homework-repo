import socket
import select
import errno
import sys
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

#===================================================================Private Helper Methods=================================================================
def _nonsession_PDU():
    pass

def _session_header(client, USERNAME):
    head = USERNAME.encode(FORMAT)
    head_len = len(head)
    send_head = str(head_len).encode(FORMAT)
    send_head += b' ' * (HEADER - len(send_head))
    client.send(send_head)
    client.send(head)

def _session_body(client, msg):
    encoded_msg = msg.encode(FORMAT)
    msg_len = len(encoded_msg)
    body_len = str(msg_len).encode(FORMAT)
    body_len += b' ' * (BODY - len(body_len))
    client.send(body_len)
    client.send(encoded_msg)


#================================================================Main Public Methods=======================================================================

def session_PDU(client, USERNAME, msg):
    _session_header(client, USERNAME)
    _session_body(client, msg)




#====================================================================Main============================================================================


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    auth = Auth()
    USERNAME = auth.authenticate()
    version = "1.0"
    code = "10"
    _nonsession_PDU()
    while True:
        msg = input(f"{USERNAME}: ")
        session_PDU(client, USERNAME, msg)


