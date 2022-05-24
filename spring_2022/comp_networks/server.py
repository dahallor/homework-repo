import socket
import threading
import pdb

HEADER = 64
BODY = 4096
PORT = 1719
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT = "EXIT" #look at DFA
CHATROOM = "\general"
ACTIVE_USERS = []
MAX_VERSION = 1.0

#=========================================================Private Helper Methods================================================================
def _decode_nonsession_PDU():
    pass

def _decode_session_PDU(conn):
    head = conn.recv(HEADER).decode(FORMAT)
    head_len = int(head)
    header = conn.recv(head_len).decode(FORMAT)
    msg = conn.recv(BODY).decode(FORMAT)
    msg_len = int(msg)
    message = conn.recv(BODY).decode(FORMAT)
    PDU = [header, message]
    return PDU

def _check_disconnect(PDU_info, connected):
    #TODO: create method to check if disconnect code is here
    connected = True
    return connected


#============================================================Main Public Methods================================================================================
def chatroom(conn, addr, header_info):
    print(f"blank has entered the chat")
    connected = True
    #TODO: change this to whatever the username is
    ACTIVE_USERS.append(header_info)
    while connected == True:
        PDU = _decode_session_PDU(conn)
        print(f"{PDU[0]}: {PDU[1]}")
        connected = _check_disconnect(PDU, connected)
    conn.close()
    #TODO: pop user from active users list

def create_threads(server):
    while True:
        conn, addr = server.accept()
        header_info = _decode_nonsession_PDU()
        new_thread = threading.Thread(target = chatroom, args = (conn, addr, header_info))
        new_thread.start()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[BOOTING UP SERVER]...")
    server.bind(ADDR)
    server.listen()
    print("[LISTENING]...")
    create_threads(server)




#=================================================================Main============================================================================

if __name__ == '__main__':
    start_server()