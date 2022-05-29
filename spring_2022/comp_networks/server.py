import socket
import threading
import pdb
from architecture import Architecture
from versions import *
from response_codes import *
from auth import *


class Server(Architecture):
    def __init__(self):
        super().__init__()
        self.CHATROOM = "&general"
        self.ACTIVE_CHATROOMS = ["&general"]
        self.ACTIVE_USERS = []
        self.ACTIVE_SOCKETS = []
        self.CHATLOG = []
        self.CONNECTIONS = {}
        self.MAX_VERSION = 1.0

    #==============================================================Private Helper Methods================================================================================
    def _check_version(self, PDU):
        if float(PDU[3]) == self.MAX_VERSION:
            PDU[0] = 21
        else:
            PDU[0] = 22
            PDU[3] = self.MAX_VERSION
        return PDU

    #=============================================================Decode/Encode Methods=================================================================================

    def _decode_nonsession_PDU(self, conn):
        head = conn.recv(self.HEADER).decode(self.FORMAT)
        head_len = int(head)
        header = conn.recv(head_len).decode(self.FORMAT)
        PDU = header.split(";")
        #Checks for correct version, returns a the accepted versions if they differ
        PDU = self._check_version(PDU)
        return PDU

    def _encode_nonsession_PDU(self, PDU, conn):
        head = ""
        for i in range(len(PDU)):
            head += str(PDU[i])
            head += self.DELIMIT
        head = head.encode(self.FORMAT)
        head_len = len(head)
        send_head = str(head_len).encode(self.FORMAT)
        send_head += b' ' * (self.HEADER - len(send_head))
        conn.send(send_head)
        conn.send(head)

    def _decode_session_PDU(self, conn, addr):
        #If client terminal force quits, this puts exit response code in header
        try:
            head = conn.recv(self.HEADER).decode(self.FORMAT)
        except ConnectionResetError:
            PDU = self.CONNECTIONS[addr]
            PDU.insert(0, 50)
            head = ""
            for i in range(len(PDU)):
                head += str(PDU[i])
                head += self.DELIMIT
            PDU = [head, None]
            return PDU

        #Else, it continues handling like normal
        head_len = int(head)
        header = conn.recv(head_len).decode(self.FORMAT)
        msg = conn.recv(self.BODY).decode(self.FORMAT)
        msg_len = int(msg)
        message = conn.recv(self.BODY).decode(self.FORMAT)
        PDU = [header, message]
        return PDU

    def _encode_session_PDU(self, PDU, msg):
        self._session_header(PDU)
        self._session_body(msg)

    def _session_header(self, PDU):
        head = ""
        PDU[0] = 32
        for i in range(len(PDU)):
            head += str(PDU[i])
            head += self.DELIMIT
        head = head.encode(self.FORMAT)
        head_len = len(head)
        send_head = str(head_len).encode(self.FORMAT)
        send_head += b' ' * (self.HEADER - len(send_head))
        for socket in self.ACTIVE_SOCKETS:
            socket.send(send_head)
            socket.send(head)

    def _session_body(self, msg):
        encoded_msg = msg.encode(self.FORMAT)
        msg_len = len(encoded_msg)
        body_len = str(msg_len).encode(self.FORMAT)
        body_len += b' ' * (self.BODY - len(body_len))
        for socket in self.ACTIVE_SOCKETS:
            socket.send(body_len)
            socket.send(encoded_msg)

    #============================================================Main Public Methods================================================================================
    def chatroom(self, v, code, conn, addr, PDU):
        print(f"[SUCCSES] {PDU[1]} has entered the chat: {self.CHATROOM}")
        self.CONNECTIONS[addr] = PDU[1:]
        self.ACTIVE_SOCKETS.append(conn)
        #While response code is not the exit response code, disseminate PDU to display messages and user info
        while int(PDU[0]) != 50:
            PDU = self._decode_session_PDU(conn, addr)
            PDU_head = PDU[0].split(";")
            PDU_body = PDU[1]
            if PDU_head[0] == code.actions["Admin Level Request"]:
                #Add method here to check admin status
                pass
            self._encode_session_PDU(PDU_head, PDU_body)
            print(f"{PDU_head[1]} >> {PDU_head[2]}: {PDU_body}")
            log_data = [PDU_head[1], PDU_head[2], PDU_body]
            self.CHATLOG.append(log_data)
            PDU = PDU_head
        print(f"[CLOSING] {PDU[1]} has left the chat: {self.CHATROOM}")
        conn.close()
        del self.CONNECTIONS[addr]
        self.ACTIVE_USERS.remove(PDU[1])
        self.ACTIVE_SOCKETS.remove(conn)
        #pdb.set_trace()

    def bad_connection(self, conn, header_info):
        print(f"[RETRYING] {header_info[1]} had bad connection request...")
        conn.close()


    def create_threads(self, v, code, server_socket):
        while True:
            conn, addr = server_socket.accept()
            header_info = self._decode_nonsession_PDU(conn)
            self._encode_nonsession_PDU(header_info, conn)
            match header_info[0]:
                #Init Failure
                case 22:
                    bad_thread = threading.Thread(target = self.bad_connection, args = (conn, header_info))
                    bad_thread.start()
                #Init Success
                case 21:
                    self.ACTIVE_USERS.append(header_info[1])
                    new_thread = threading.Thread(target = self.chatroom, args = (v, code, conn, addr, header_info))
                    new_thread.start()
                case _:
                    #This should never trigger, but match/case can act fickle if a catch-all case is not included
                    raise Exception("Init Check returning invalid value")

    def start_server(self, v, code):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[BOOTING UP SERVER]...")
        server_socket.bind(self.ADDR)
        server_socket.listen()
        print("[LISTENING]...")
        self.create_threads(v, code, server_socket)




#=================================================================Main============================================================================

if __name__ == '__main__':
    v = Versions()
    code = Codes()
    s = Server()
    s.start_server(v, code)