import socket
import threading
import sys
import pdb
from architecture import Architecture
from auth import *
from response_codes import *
from versions import *
from gui import *


class Client(Architecture):
    def __init__(self):
        super().__init__()
        self.user = ""
        self.active_version = 0


#===================================================================Private Helper Methods=================================================================
    def _eval_response_code(self, code, v, PDU, msg):
        PDU[0] = code.actions["Push MSG To Server"]
        if msg in v.admin_permissions[self.active_version] and PDU[3] == True:
            PDU[0] = code.actions["Admin Level Request"]
        if msg in v.versions[self.active_version] and msg not in v.admin_permissions[self.active_version] and msg != "!exit":
            PDU[0] = code.actions["Nonadmin Command"]
        if msg == "!exit":
            PDU[0] = code.actions["Exit"]
        print(PDU)
        return PDU
        
    def _encode_nonsession_PDU(self, client_socket, PDU, code):
        head = ""
        for i in range(len(PDU)):
            head += str(PDU[i])
            if i != len(PDU)-1:
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

    def _encode_session_PDU(self, v, code, client_socket, PDU, msg):
        print(f"encodeing: {PDU}")
        PDU = self._eval_response_code(code, v, PDU, msg)
        self._session_header(client_socket, PDU)
        self._session_body(client_socket, msg)


    def _decode_session_PDU(self, client_socket):
        head = client_socket.recv(self.HEADER).decode(self.FORMAT)
        head_len = int(head)
        header = client_socket.recv(head_len).decode(self.FORMAT)
        msg = client_socket.recv(self.BODY).decode(self.FORMAT)
        msg_len = int(msg)
        message = client_socket.recv(msg_len).decode(self.FORMAT)
        PDU = [header, message]
        return PDU
        

    def _session_header(self, client_socket, PDU):
        print(f"session header: {PDU}")
        head = ""
        for i in range(len(PDU)):
            head += str(PDU[i])
            if i != len(PDU)-1:
                head += self.DELIMIT
        head = head.encode(self.FORMAT)
        head_len = len(head)
        send_head = str(head_len).encode(self.FORMAT)
        send_head += b' ' * (self.HEADER - len(send_head))
        print(f"sending: {head}")
        client_socket.send(send_head)
        client_socket.send(head)

    def _session_body(self, client_socket, msg):
        encoded_msg = msg.encode(self.FORMAT)
        msg_len = len(encoded_msg)
        body_len = str(msg_len).encode(self.FORMAT)
        body_len += b' ' * (self.BODY - len(body_len))
        print(f"sending body: {encoded_msg}")
        client_socket.send(body_len)
        client_socket.send(encoded_msg)

    def _welcome_msg(self):
        print("\nHello there! Welcome to Discourse!")
        print("Use the following commands:\n& notates a chatroom. \n! notates a command\nTo switch to a new chatroom, type '!switch &[CHATROOM]'\nAll users can view available chatrooms. Use '!list' to list them.\nAccounts with admin privledges can add and remove chatrooms. Use '!add' and '!del' respectively\nTo close, type '!exit'\n")


    #================================================================Main Public Methods=======================================================================

    def rec_loop(self, v, code, gui, client_socket):
        while True:
            print("in rec loop")
            PDU = self._decode_session_PDU(client_socket)
            PDU_head = PDU[0].split(";")
            PDU_body = PDU[1]
            print(self.user, PDU_head)
            if PDU_head[2] != self.user:
                gui._enter_others_msg(PDU_head[2], PDU_body)
                #print(f"{PDU_head[2]} >> {PDU_body}: ")
            PDU = PDU_head

    def send_loop(self, v, code, gui, PDU, client_socket):
        listen_thread = threading.Thread(target=self.rec_loop, args=(v, code, gui, client_socket))
        listen_thread.start()
        while True:
            msg = input(f"{PDU[1]} >> {PDU[2]}: ")
            self._encode_session_PDU(v, code, client_socket, PDU, msg)



    def start_client(self, auth, code, v, gui):
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
        self.active_version = float(PDU_header[3])

        #TODO: implement functionality of the welcome message
        self._welcome_msg()
        gui.run_GUI(v, code, PDU, client_socket)




#====================================================================Main============================================================================


if __name__ == '__main__':
    auth = Auth()
    code = Codes()
    v = Versions()
    c = Client()
    gui = GUI(c)

    c.start_client(auth, code, v, gui)



