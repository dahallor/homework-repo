import socket
import threading
import pdb

HEADER = 64
PORT = 1719
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'
DISCONNECT = "EXIT" #look at DFA
CHATROOM = "\general"
ACTIVE_USERS = []

#=========================================================Private Helper Methods================================================================
def _decode_nonsession_PDU():
    pass

def _decode_session_PDU():
    msg = SERVER.recv()

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
        PDU_info = _decode_session_PDU()
        connected = _check_disconnect(PDU_info, connected)
    conn.close()
    #TODO: pop user from active users list

def create_threads():
    while True:
        conn, addr = SERVER.accept()
        header_info = _decode_nonsession_PDU()
        new_thread = threading.Thread(target = chatroom, args = (conn, addr, header_info))
        new_thread.start()

def start_server():
    print("[BOOTING UP SERVER]...")
    SERVER.bind(ADDR)
    SERVER.listen()
    print("[LISTENING]...")
    create_threads()




#=================================================================Main============================================================================

if __name__ == '__main__':
    start_server()