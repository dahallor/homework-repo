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
CHATROOM = "&general"
ACTIVE_USERS = []
MAX_VERSION = 1.0
DELIMIT = ";"
END = "\n\n"

#=========================================================Private Helper Methods================================================================
def _check_version(PDU):
    if float(PDU[3]) == MAX_VERSION:
        PDU[0] = 21
    else:
        PDU[0] = 22
        PDU[3] = MAX_VERSION
    return PDU

def _decode_nonsession_PDU(conn):
    head = conn.recv(HEADER).decode(FORMAT)
    head_len = int(head)
    header = conn.recv(head_len).decode(FORMAT)
    PDU = header.split(";")
    PDU = _check_version(PDU)
    return PDU

def _encode_nonsession_PDU(PDU, conn):
    head = ""
    for i in range(len(PDU)):
        head += str(PDU[i])
        head += DELIMIT
    head += END
    head = head.encode(FORMAT)
    head_len = len(head)
    send_head = str(head_len).encode(FORMAT)
    send_head += b' ' * (HEADER - len(send_head))
    conn.send(send_head)
    conn.send(head)

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
    print(f"[SUCCSES] {header_info[1]} has entered the chat: {CHATROOM}")
    connected = True
    ACTIVE_USERS.append(header_info[1])
    while connected == True:
        PDU = _decode_session_PDU(conn)
        PDU_head = PDU[0].split(";")
        PDU_body = PDU[1]
        print(f"{PDU_head[1]} >> {PDU_head[2]}: {PDU_body}")
        connected = _check_disconnect(PDU, connected)
    conn.close()
    #TODO: pop user from active users list

def bad_connection(conn, header_info):
    print(f"[RETRYING] {header_info[1]} had bad connection request...")
    conn.close()


def create_threads(server):
    while True:
        conn, addr = server.accept()
        header_info = _decode_nonsession_PDU(conn)
        _encode_nonsession_PDU(header_info, conn)
        match header_info[0]:
            case 22:
                bad_thread = threading.Thread(target = bad_connection, args = (conn, header_info))
                bad_thread.start()
            case 21:
                new_thread = threading.Thread(target = chatroom, args = (conn, addr, header_info))
                new_thread.start()
            case _:
                raise Exception("Init Check returning invalid value")

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