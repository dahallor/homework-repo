class Versions:
    def __init__(self):
        self.versions = {1.0 : ["!switch", "!add", "!del", "!list", "!exit"], 1.1 : "What's my job? Debugging purposes"}
        self.admin_permissions = {1.0 : ["!add", "!del"]}

    '''
    def add_new_version(self):
        #For Extention
        new_version = input("Enter new verion number")
        features = []
        if new_version not in self.versions:
            self.versions[new_version] = features
    '''

    def get_max_version(self):
        max = 0
        for key in self.versions:
            if key > max:
                max = key
        return max


        