class Codes:
    def __init__(self):
        self.codes = {
        10 : "Login Request",
        11 : "Auth Success",
        12 : "Auth Fail",
        20 : "Init Request",
        21 : "Init Success",
        22 : "Init Fail",
        31 : "Push MSG To Server",
        32 : "Push MSG To Clients",
        33 : "Nonadmin Command",
        40 : "Admin Level Request",
        41 : "Admin Level Rejected",
        42 : "Admin Level Command",
        50 : "Exit"}

        self.actions = {
        "Login Request" : 10,
        "Auth Success" : 11,
        "Auth Fail" : 12,
        "Init Request" : 20,
        "Init Success" : 21,
        "Init Fail" : 22,
        "Push MSG To Server" : 31,
        "Push MSG To Clients" : 32,
        "Nonadmin Command" : 33,
        "Admin Level Request" : 40,
        "Admin Level Rejected" : 41,
        "Admin Level Command" : 42,
        "Exit" : 50}
        