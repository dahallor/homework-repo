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

    def _authenticate(self, verify, username, password):
        try:
            self.login[username]
        except KeyError:
            print("Username not recognized\n")
            return verify
        try:
            pswd = self.login[username]
            if pswd != password:
                raise Exception
        except Exception:
            print("Incorrect password\n")
            return verify

        verify = True
        return verify

    def authenticate(self): 
        verify = False
        while verify == False:
            username = input("Username: ")
            password = input("Password: ")
            verify = self._authenticate(verify, username, password)
        return username

'''      
if __name__ == '__main__':
    a = Auth()
    a.authenticate()
'''
