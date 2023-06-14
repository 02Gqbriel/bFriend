class User:
    user_id: int = None
    firstname: str = None
    email: str = None
    lastname: str = None
    username: str = None
    age: int = None
    password: str = None
    hobby: str = None
    acc_status: str = None

    def __init__(self, username: str, password: str):
        self.username: str = username
        self.password: str = password

    def set_user_id(self, user_id: int):
        self.user_id = user_id
        return

    def set_firstname(self, firstname: str):
        self.firstname = firstname
        return

    def set_lastname(self, lastname: str):
        self.lastname = lastname
        return

    def set_email(self, email: str):
        self.email = email
        return

    def set_username(self, username: str):
        self.username = username
        return

    def set_age(self, age: int):
        self.age = age
        return

    def set_password(self, password: str):
        self.password = password
        return

    def set_hobby(self, hobby: str):
        self.hobby = hobby
        return

    def set_acc_status(self, acc_status: str):
        self.acc_status = acc_status
        return
