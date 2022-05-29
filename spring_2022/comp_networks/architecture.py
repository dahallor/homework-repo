from abc import abstractclassmethod
import socket

class Architecture:
    def __init__(self):
        self.HEADER = 64
        self.BODY = 4096
        self.PORT = 1719
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'UTF-8'
        self.DELIMIT = ";"

    @abstractclassmethod
    def _encode_nonsession_PDU(self):
        pass

    @abstractclassmethod
    def _decode_nonsession_PDU(self):
        pass

    @abstractclassmethod
    def _encode_session_PDU(self):
        pass

    @abstractclassmethod
    def _decode_session_PDU(self):
        pass

