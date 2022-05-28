class Versions:
    def __init__(self):
        self.versions = {1.0 : ["switch chatroom", "add chatroom", "del chatroom", "list chatrooms"], 1.1 : "What's my job? Debugging purposes"}
        self.admin_permissions = {1.0 : ["add chatroom", "del chatroom", "list chatrooms"]}

    def add_new_versrion(self):
        #For Extention
        new_version = input("Enter new verion number")
        features = []
        if new_version not in self.versions:
            self.versions[new_version] = features

    def get_max_version(self):
        max = 0
        for key in self.versions:
            if key > max:
                max = key
        return max

    def get_in_use_version(self, PDU):
        #If a server has only accepts a lower version than the max, this alters the client version to match the servers
        pass
        