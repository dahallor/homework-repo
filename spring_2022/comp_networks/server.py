import socket
import threading
import pdb
from architecture import Architecture
from versions import *
from response_codes import *
from auth import *
from commands import *


class Server(Architecture):
    def __init__(self):
        super().__init__()
        self.CHATROOM = "&general"
        self.ACTIVE_CHATROOMS = ["&general", "&private"]
        self.ACTIVE_USERS = []
        self.ACTIVE_SOCKETS = []
        self.CHATLOG = []
        self.CONNECTIONS = {}
        self.MAX_VERSION = 1.0
        self.CLEAR_SCREEN = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

#==============================================================Private Helper Methods================================================================================
    def _str_to_bool(self, value):
        if value == "False":
            return_val = False
        if value == "True":
            return_val = True
        return return_val
    
    def _check_version(self, PDU):
        if float(PDU[3]) == self.MAX_VERSION:
            PDU[0] = 21
        else:
            PDU[0] = 22
            PDU[3] = self.MAX_VERSION
        return PDU


    def _system_cmds(self, code, PDU_header, PDU_body):
        #pdb.set_trace()
        PDU_body_list = PDU_body.split(" ")
        print(f"special commands: {PDU_header} {PDU_body}")
        try:
            pdu_list = PDU_body.split(" ")
            chatroom_delimiter = pdu_list[1][0]
        except IndexError:
            chatroom_delimiter = None
        
        
        if int(PDU_header[0]) == code.actions["Admin Level Request"]:
            admin_level = self._str_to_bool(PDU_header[3])
            if admin_level == False:
                PDU_header[0] = code.actions["Admin Level Rejected"]
            if admin_level == True:
                exe_cmd = False
                if PDU_body_list[0] == "!add" and chatroom_delimiter == "&":
                        self.ACTIVE_CHATROOMS.append(PDU_body_list[1])
                        print(f"{PDU_body_list[1]} added!")
                        PDU_header[0] = code.actions["Admin Level Command"]
                        PDU_header[2] = "sys"
                        exe_cmd = True
                if PDU_body_list[0] == "!del" and chatroom_delimiter == "&":
                        self.ACTIVE_CHATROOMS.remove(PDU_body_list[1])
                        print(f"{PDU_body_list[1]} removed!")
                        PDU_header[2] = "sys"
                        if PDU_body_list[1] != "&general":
                            to_delete = []
                            for i in range(len(self.CHATLOG)):
                                if PDU_body_list[1] == self.CHATLOG[i][0]:
                                    to_delete.append(self.CHATLOG[i])
                            for i in range(len(to_delete)):
                                self.CHATLOG.remove(to_delete[i])
                            exe_cmd = True
                        if PDU_body_list[1] == "&general":
                            PDU_body = "Cannot delete '&general' chatroom"
                if exe_cmd == True:
                    PDU_header[0] = code.actions["Admin Level Command"]
                if exe_cmd == False:
                    PDU_header[0] = code.actions["Admin Level Rejected"]
            #pdb.set_trace()
    

        if int(PDU_header[0]) == code.actions["Push MSG To Server"]:
            PDU_header[0] = code.actions["Push MSG To Clients"]


        if int(PDU_header[0]) == code.actions["Switch Chatroom"]:
            #pdb.set_trace()
            if chatroom_delimiter == "&" and PDU_body_list[1] in self.ACTIVE_CHATROOMS:
                PDU_header[1] = PDU_body_list[1]
                PDU_body = ""
                for i in range(len(self.CHATLOG)):
                    if PDU_header[1] == self.CHATLOG[i][0]:
                        PDU_body += f"{self.CHATLOG[i][1]}: {self.CHATLOG[i][2]}\n"


        if int(PDU_header[0]) == code.actions["List Chatrooms"]:
            #PDU_header[2] = "sys"
            PDU_body = ""
            for chatroom in self.ACTIVE_CHATROOMS:
                PDU_body += chatroom
                PDU_body += " "

        print(f"system eval: {PDU_header} {self.ACTIVE_CHATROOMS}")
        return PDU_header, PDU_body

#=============================================================Decode/Encode Methods=================================================================================

    def _decode_nonsession_PDU(self, conn):
        head = conn.recv(self.HEADER).decode(self.FORMAT)
        head_len = int(head)
        header = conn.recv(head_len).decode(self.FORMAT)
        PDU = header.split(";")
        #Checks for correct version, returns the accepted versions if they differ
        PDU = self._check_version(PDU)
        return PDU

    def _encode_nonsession_PDU(self, PDU, conn):
        head = ""
        for i in range(len(PDU)):
            head += str(PDU[i])
            if i != len(PDU)-1:
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
                if i != len(PDU)-1:
                    head += self.DELIMIT
            PDU = [head, None]
            return PDU

        #Else, it continues handling like normal
        head_len = int(head)
        header = conn.recv(head_len).decode(self.FORMAT)
        msg = conn.recv(self.BODY).decode(self.FORMAT)
        msg_len = int(msg)
        message = conn.recv(msg_len).decode(self.FORMAT)
        PDU = [header, message]
        print(f"decode session: {PDU} {header} {message}")
        return PDU

    def _encode_session_PDU(self, code, commands, PDU, msg):
        print(f'encoding: {PDU} {msg}')
        self._session_header(PDU)
        self._session_body(msg)

    def _session_header(self, PDU):
        head = ""
        for i in range(len(PDU)):
            head += str(PDU[i])
            if i != len(PDU)-1:
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
    def chatroom(self, v, code, commands, conn, addr, PDU):
        print(f"[SUCCSES] {PDU[1]} has entered the chat")
        self.CONNECTIONS[addr] = PDU[1:]
        self.ACTIVE_SOCKETS.append(conn)
        #While response code is not the exit response code, disseminate PDU to display messages and user info
        while True:
            #Decode recv message
            PDU = self._decode_session_PDU(conn, addr)
            PDU_head = PDU[0].split(";")
            PDU_body = PDU[1]

            #Check for certain special commands
            PDU_head, PDU_body = self._system_cmds(code, PDU_head, PDU_body)

            #send data back to clients
            self._encode_session_PDU(code, commands, PDU_head, PDU_body)
            
            #Archiving
            if int(PDU_head[0]) != code.actions["Switch Chatroom"] and int(PDU_head[0]) != code.actions["List Chatrooms"] and PDU_head[2] != "sys":
                log_data = [PDU_head[1], PDU_head[2], PDU_body]
                self.CHATLOG.append(log_data)
            PDU = PDU_head
    
            #Exit
            if int(PDU[0]) == code.actions["Exit"]:
                break
        
        #Closing Connection
        print(f"[CLOSING] {PDU[2]} has left the chat")
        conn.close()
        del self.CONNECTIONS[addr]
        self.ACTIVE_USERS.remove(PDU[2])
        self.ACTIVE_SOCKETS.remove(conn)


    def bad_connection(self, conn, header_info):
        print(f"[RETRYING] {header_info[1]} had bad connection request...")
        conn.close()


    def create_threads(self, v, code, commands, server_socket):
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
                    new_thread = threading.Thread(target = self.chatroom, args = (v, code, commands, conn, addr, header_info))
                    new_thread.start()
                case _:
                    #This should never trigger, but match/case can act fickle if a catch-all case is not included
                    raise Exception("Init Check returning invalid value")

    def start_server(self, v, code, commands):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[BOOTING UP SERVER]...")
        server_socket.bind(self.ADDR)
        server_socket.listen()
        print("[LISTENING]...")
        self.create_threads(v, code, commands, server_socket)




#=================================================================Main============================================================================

if __name__ == '__main__':
    v = Versions()
    code = Codes()
    s = Server()
    commands = Cmds(s)
    s.start_server(v, code, commands)