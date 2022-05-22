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

#=========================================================Private Helper Methods================================================================

def _decode_NonSession_PDU(connection):
    try:
        head_len = connection.recv(HEADER).decode(FORMAT)
        #pdb.set_trace()
        head_len = int(len(head_len))
        head = connection.recv(head_len).decode(FORMAT)
        head = head.strip("\n")
        header_info = head.split(";")
        pdb.set_trace()
        print(f"{header_info[2]} has entered the chat.")
    except Exception:
        raise Exception("Failed to Parse Header Info")

def _decode_Session_PDU(connection):
    msg_len = connection.recv(HEADER).decode(FORMAT)
    msg_len = int(msg_len)
    msg = connection.recv(msg_len).decode(FORMAT)
    pdb.set_trace()


def _check_Connection(msg, connected):
    if msg == DISCONNECT:
        connected = False
        print(f"\\blank has left the chat.")
    else:
        print(f"blank {msg}")
    return connected

#=============================================Main Public Methods================================================================================

def client_handler(connection, address):
    _decode_NonSession_PDU(connection)
    connected = True
    while connected:
        try:
            msg = _decode_Session_PDU(connection)
            connected = _check_Connection(msg, connected)
        except:
            pass
    connection.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING]...\nWelcome to {CHATROOM}!")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = client_handler, args = (conn, addr))
        thread.start()
        #print(f"num connections: {threading.active_count() -1}")


#=================================================================Main============================================================================

if __name__ == '__main__':
    print("[START SERVER]...")
    start_server()