from server import *

class Cmds(Server):
    def __init__(self):
        super().__init__()

    def _load_chatlog(self, chatroom):
        for log in self.CHATLOG:
            target_chatroom = log[0]
            if chatroom == target_chatroom:
                print(f"{log[0]} >> {log[1]}: {log[2]}")

    def special_cmds(self, code, PDU_header, PDU_body):
        PDU_body = PDU_body.split(" ")
        print(f"special commands: {PDU_header} {PDU_body}")
        try:
            chatroom_delimiter = PDU_body[1][0]
        except IndexError:
            chatroom_delimiter = None
        if PDU_header[0] == code.actions["Admin Level Command"]:
            match PDU_body:
                case "!add":
                    if chatroom_delimiter == "&":
                        self.ACTIVE_CHATROOMS.append(PDU_body[1])
                        print(f"{PDU_body[1]} added!")
                case "!del":
                    if chatroom_delimiter == "&":
                        self.ACTIVE_CHATROOMS.remove(PDU_body[1])
                        print(f"{PDU_body[1]} removed!")
                case _:
                    raise Exception("Admin command issue")
        if PDU_header[0] == code.actions["Nonadmin Command"]:
            match PDU_body:
                case "!switch":
                    if chatroom_delimiter == "&":
                        PDU_header[1] = PDU_body[1]
                        print(self.CLEAR_SCREEN)
                        print(f"Switched to {PDU_body[1]}")
                        self._load_chatlog(PDU_body[1])
                case "!list":
                    for chatroom in self.ACTIVE_CHATROOMS:
                        print(f"{chatroom}")
                case "!exit":
                    PDU_header[0] = code.actions["Exit"]
                case _:
                    raise Exception("Nonadmin command issue")
        return PDU_header