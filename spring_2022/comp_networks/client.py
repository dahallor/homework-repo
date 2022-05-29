import socket
import select
import errno
import sys
import pdb
from architecture import Architecture
from auth import *
from response_codes import *
from versions import *


class Client(Architecture):
    def __init__(self):
        super().__init__()
        self.user = ""


    #===================================================================Private Helper Methods=================================================================
    def _encode_nonsession_PDU(self, client_socket, PDU, code):
        head = ""
        for i in range(len(PDU)):
            head += str(PDU[i])
            head += self.DELIMIT
        head = head.encode(self.FORMAT)
        head_len = len(head)
        send_head = str(head_len).encode(self.FORMAT)
        send_head += b' ' * (self.HEADER - len(send_head))
        client_socket.send(send_head)
        client_socket.send(head)

    def _decode_nonsession_PDU(self, client_socket, PDU, code):
        head = client_socket.recv(self.HEADER).decode(self.FORMAT)
        head_len = int(head)
        header = client_socket.recv(head_len).decode(self.FORMAT)
        PDU = header.split(";")
        return PDU

    def _encode_session_PDU(self, client_socket, PDU, msg):
        self._session_header(client_socket, PDU)
        self._session_body(client_socket, msg)

    def _decode_session_PDU(self, client_socket):
        head = client_socket.recv(self.HEADER).decode(self.FORMAT)
        head_len = int(head)
        header = client_socket.recv(head_len).decode(self.FORMAT)
        msg = client_socket.recv(self.BODY).decode(self.FORMAT)
        msg_len = int(msg)
        message = client_socket.recv(self.BODY).decode(self.FORMAT)
        PDU = [header, message]
        return PDU
        

    def _session_header(self, client_socket, PDU):
        head = ""
        for i in range(len(PDU)):
            head += str(PDU[i])
            head += self.DELIMIT
        head = head.encode(self.FORMAT)
        head_len = len(head)
        send_head = str(head_len).encode(self.FORMAT)
        send_head += b' ' * (self.HEADER - len(send_head))
        client_socket.send(send_head)
        client_socket.send(head)

    def _session_body(self, client_socket, msg):
        encoded_msg = msg.encode(self.FORMAT)
        msg_len = len(encoded_msg)
        body_len = str(msg_len).encode(self.FORMAT)
        body_len += b' ' * (self.BODY - len(body_len))
        client_socket.send(body_len)
        client_socket.send(encoded_msg)

    def _welcome_msg(self):
        print("\nHello there! Welcome to Discourse!")
        print("Use the following commands:\n& notates a chatroom. \nTo switch to a different chatroom, type '&[CHATROOM NAME]'\n! notates a command\nAll users can view available chatrooms. Use '!list' to list them.\nAccounts with admin privledges can add and remove chatrooms. Use '!add' and '!del' respectively\nTo close, type '!exit'\n")


    #================================================================Main Public Methods=======================================================================



    def main_loop(self, PDU, client_socket):
        while True:
            print(PDU)
            msg = input(f"{PDU[1]} >> {PDU[2]}: ")
            self._encode_session_PDU(client_socket, PDU, msg)
            PDU = self._decode_session_PDU(client_socket)
            PDU_head = PDU[0].split(";")
            PDU_body = PDU[1]
            if PDU_head[2] != self.user:
                print(f"{PDU_head[2]} >> {PDU_body}: ")
            PDU = PDU_head


    def start_client(self, auth, code, v):
        PDU_header = []

        auth.authenticate(PDU_header, code)
        PDU_header.append(v.get_max_version())

        PDU_header[0] = code.actions["Init Request"]
        while int(PDU_header[0]) == code.actions["Init Request"] or int(PDU_header[0]) == code.actions["Init Fail"]:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(self.ADDR)
            self._encode_nonsession_PDU(client_socket, PDU_header, code)
            PDU_header = self._decode_nonsession_PDU(client_socket, PDU_header, code)
        #Reponse code, chatroom, username, admin status       
        PDU = [31, "&general", PDU_header[1], PDU_header[2]]
        self.user = PDU[2]

        #TODO: implement functionality of the welcome message
        self._welcome_msg()
        self.main_loop(PDU, client_socket)



#====================================================================Main============================================================================


if __name__ == '__main__':
    auth = Auth()
    code = Codes()
    v = Versions()
    c = Client()

    c.start_client(auth, code, v)



