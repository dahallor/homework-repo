import socket
import select
import errno
import sys
import pdb
from auth import *
from gui import *

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
class Client:
    def __init__(self, client_socket, USERNAME):
        self.client_socket = client_socket
        self.USERNAME = USERNAME

    def _nonsession_PDU(self):
        pass

    def _session_header(self, client_socket, USERNAME):
        head = USERNAME.encode(FORMAT)
        head_len = len(head)
        send_head = str(head_len).encode(FORMAT)
        send_head += b' ' * (HEADER - len(send_head))
        client_socket.send(send_head)
        client_socket.send(head)

    def _session_body(self, client_socket, msg):
        encoded_msg = msg.encode(FORMAT)
        msg_len = len(encoded_msg)
        body_len = str(msg_len).encode(FORMAT)
        body_len += b' ' * (BODY - len(body_len))
        client_socket.send(body_len)
        client_socket.send(encoded_msg)


    #================================================================Main Public Methods=======================================================================

    def session_PDU(self, client, USERNAME, msg):
        self._session_header(client, USERNAME)
        self._session_body(client, msg)




#====================================================================Main============================================================================


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)
    auth = Auth()
    USERNAME = auth.authenticate()
    gui = GUI(client_socket, USERNAME)


    version = "1.0"
    code = "10"
    gui._nonsession_PDU()
    gui.run_GUI()

        


