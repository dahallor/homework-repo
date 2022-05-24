#Add a "create user" function
#Verify a username/password is under a ceertain byte limit
#verify only one person is logged in under one username at a time


class Auth:
    def __init__(self):
        self.login = {
        "IsDiscourseBestProto?" : "ItDepends!121",
        "CryptoBro121" : "IFailedEcon101",
        "test" : "test"
        }

    def _not_logged_in(self):
        #TODO: place some code here
        pass



    def _authenticate(self, verify, username, password):
        #Attempt to login with unknown username
        try:
            self.login[username]
        except KeyError:
            print("Username not recognized\n")
            return verify

        #Attempt to login with incorrect password
        try:
            pswd = self.login[username]
            if pswd != password:
                raise Exception
        except Exception:
            print("Incorrect password\n")
            return verify

        #Attempt to login to an account already logged in
        #TODO: place some code here

        verify = True
        return verify

    def authenticate(self): 
        verify = False
        while verify == False:
            username = input("Username: ")
            password = input("Password: ")
            verify = self._authenticate(verify, username, password)
        print(f"Willkommen {username}!")
        return username

    def create_new_account(self):
        #TODO: add shit here
        pass
