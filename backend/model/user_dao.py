from backend.connect import connect_database
from backend.model.user import User


def select_all():
    return connect_database("SELECT * FROM User")


def select_user(user_id: int):
    response = connect_database("SELECT * FROM User WHERE userID = ?", user_id)
    return response


def create_user(user: User):
    response = connect_database(
        "INSERT INTO User (username, password, firstname, lastname, age, hobby, accStatus) VALUES (?, ?, ?, ?, ?, ?, ?)",
        user.username, user.password, user.firstname, user.lastname, user.age, user.hobby, user.acc_status)
    return response


def update_user(user: User):
    response = connect_database(
        "UPDATE User SET username=?, password=?, firstname=?, lastname=?, age=?, hobby=?, accStatus=? WHERE userID=?",
        user.username, user.password, user.firstname, user.lastname, user.age, user.hobby,
        user.acc_status, user.user_id)
    return response


def delete_user(user_id: int):
    response = connect_database("DELETE FROM User WHERE userID = ?", user_id)
    return response
