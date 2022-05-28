import socket
import select
import errno
import sys
import pdb
from auth import *
from response_codes import *
from versions import *

#Add functionality for DMing or main chat room. delimit it by backslash. Look up how to make seperate chat rooms

HEADER = 64
BODY = 4096
PORT = 1719
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT = "EXIT" #look at DFA
DELIMIT = ";"
END = "\n\n"

#===================================================================Private Helper Methods=================================================================
def _encode_nonsession_PDU(client, PDU, code):
    head = ""
    for i in range(len(PDU)):
        head += str(PDU[i])
        head += DELIMIT
    #head += END
    head = head.encode(FORMAT)
    head_len = len(head)
    send_head = str(head_len).encode(FORMAT)
    send_head += b' ' * (HEADER - len(send_head))
    client.send(send_head)
    client.send(head)

def _decode_nonsession_PDU(client, PDU, code):
    head = client.recv(HEADER).decode(FORMAT)
    head_len = int(head)
    header = client.recv(head_len).decode(FORMAT)
    PDU = header.split(";")
    return PDU
    

def _session_header(client, PDU):
    head = ""
    for i in range(len(PDU)):
        head += str(PDU[i])
        head += DELIMIT
    #head += END
    head = head.encode(FORMAT)
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

def _welcome_msg():
    print("\nHello there! Welcome to Discourse!")
    print("Use the following commands:\n& notates a chatroom. \nTo switch to a different chatroom, type '&[CHATROOM NAME]'\nAll users can view available chatrooms. Use '&list' to list them.\nAccounts with admin privledges can add and remove chatrooms. Use '&add' and '&del' respectively\nTo close, type '&exit'\n")


#================================================================Main Public Methods=======================================================================

def encode_session_PDU(client, PDU, msg):
    _session_header(client, PDU)
    _session_body(client, msg)




#====================================================================Main============================================================================


if __name__ == '__main__':
    auth = Auth()
    code = Codes()
    v = Versions()
    PDU_header = []

    auth.authenticate(PDU_header, code)
    PDU_header.append(v.get_max_version())



    PDU_header[0] = code.actions["Init Request"]
    while int(PDU_header[0]) == code.actions["Init Request"] or int(PDU_header[0]) == code.actions["Init Fail"]:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        _encode_nonsession_PDU(client, PDU_header, code)
        PDU_header = _decode_nonsession_PDU(client, PDU_header, code)
    #Reponse code, chatroom, username, admin status       
    PDU = [31, "&general", PDU_header[1], PDU_header[2]]
    #TODO: implement functionality of the welcome message
    _welcome_msg()
    while True:
        msg = input(f"{PDU[1]} >> {PDU[2]}: ")
        encode_session_PDU(client, PDU, msg)


