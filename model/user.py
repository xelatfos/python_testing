class User(object):
    def __init__(self, login, password, fullName = ""):
        self.login = login
        self.password = password
        self.fullName = fullName