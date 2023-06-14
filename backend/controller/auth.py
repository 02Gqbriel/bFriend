from flask import Blueprint, request, make_response
from backend.model.user import User
from backend.model.user_dao import create_user, select_user, select_all

blueprint = Blueprint("auth", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form["password"]

    all_users = select_all()

    for user in all_users:
        if user.username == username and user.password == password:
            response = make_response("success")
            response.set_cookie("user_id", str(user.user_id))
            return response

    return "Login failed: invalid username or password"


@blueprint.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    age = request.form['age']
    hobby = request.form['hobby']
    acc_status = "Active"

    user = User(username, password, email, firstname, lastname, age, hobby, acc_status)

    create_user(user)

    return "successful"
