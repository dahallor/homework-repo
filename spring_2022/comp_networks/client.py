import socket
import select
import errno
import sys
import pdb
from auth import *

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


#================================================================Main Public Methods=======================================================================






#====================================================================Main============================================================================


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    auth = Auth()
    USERNAME = auth.authenticate()
    version = "1.0"
    code = "10"
    while True:
        pass

