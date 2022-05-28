#Add a "create user" function
#Verify a username/password is under a ceertain byte limit
#verify only one person is logged in under one username at a time


class Auth:
    def __init__(self):
        self.login = {
        "IsDiscourseBestProto?" : ["ItDepends!121", True],
        "CryptoBro121" : ["IFailedEcon101", False],
        "test" : ["test", False],
        "debug" : ["debug", True]
        }

    def _not_logged_in(self):
        #TODO: place some code here
        pass



    def _authenticate(self, username, password, code):
        #Attempt to login with unknown username
        try:
            self.login[username]
        except KeyError:
            print("Username not recognized\n")
            return code.actions["Auth Failed"]

        #Attempt to login with incorrect password
        try:
            pswd = self.login[username]
            if pswd[0] != password:
                raise Exception
        except Exception:
            print("Incorrect password\n")
            return code.actions["Auth Failed"]

        #Attempt to login to an account already logged in
        #TODO: place some code here

        return code.actions["Auth Success"]

    def authenticate(self, PDU, code): 
        PDU.append(code.actions["Login Request"])
        #Inifinite loop until function returns rep code 11: Auth Success
        while PDU[0] == code.actions["Login Request"] or PDU[0] == code.actions["Auth Fail"]:
            username = input("Username: ")
            password = input("Password: ")
            PDU[0] = self._authenticate(username, password, code)
        print(f"Willkommen {username}!")
        PDU.append(username)
        admin_status = self.login[username]
        PDU.append(admin_status[1])
        return PDU

    def create_new_account(self):
        #TODO: add shit here
        pass

    def admin(self):
        #TODO: add shit here for admin permission
        pass
