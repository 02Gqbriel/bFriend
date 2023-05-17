class User:
    def __int__(self, userID, prename, lastname, username, password, hobby, accStatus):
        self.userID = userID
        self.prename = prename
        self.lastname = lastname
        self.username = username
        self.password = password
        self.hobby = hobby
        self.accStatus = accStatus

    def __int__(self, userID, username, password):
        self.userID = userID
        self.prename = None
        self.lastname = None
        self.username = username
        self.password = password
        self.hobby = None
        self.accStatus = None

