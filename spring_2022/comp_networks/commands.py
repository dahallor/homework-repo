import pdb

class Cmds:
    def __init__(self, server):
        super().__init__()
        self.server = server

    '''
    def _load_chatlog(self, chatroom):
        for log in self.CHATLOG:
            target_chatroom = log[0]
            if chatroom == target_chatroom:
                print(f"{log[0]} >> {log[1]}: {log[2]}")

    def special_cmds(self, code, PDU_header, PDU_body):
        #pdb.set_trace()
        PDU_body_list = PDU_body.split(" ")
        print(f"special commands: {PDU_header} {PDU_body}")
        try:
            chatroom_delimiter = PDU_body[1][0]
        except IndexError:
            chatroom_delimiter = None
        
        match int(PDU_header[0]):
            case code.actions["Admin Level Command"]:
                if PDU_body_list[0] == "!add" and chatroom_delimiter == "&":
                        self.server.ACTIVE_CHATROOMS.append(PDU_body_list[1])
                        print(f"{PDU_body_list[1]} added!")
                if PDU_body_list[0] == "!del" and chatroom_delimiter == "&":
                        self.server.ACTIVE_CHATROOMS.remove(PDU_body_list[1])
                        print(f"{PDU_body_list[1]} removed!")
        

            case code.actions["Push MSG To Server"]:
                PDU_header[0] = code.actions["Push MSG To Clients"]

            case code.actions["Switch Chatroom"]:
                pdb.set_trace()
                if chatroom_delimiter == "&":
                    PDU_header[1] = PDU_body_list[1]
                    print(f"Switched to {PDU_body_list[1]}")
                    self._load_chatlog(PDU_body_list[1])
            case code.actions["List Chatrooms"]:
                PDU_header[2] = "sys"
                PDU_body = ""
                for chatroom in self.server.ACTIVE_CHATROOMS:
                    PDU_body += chatroom
                    PDU_body += " "
            case _:
                raise Exception("System Commands Issue")


        return PDU_header, PDU_body
        '''
