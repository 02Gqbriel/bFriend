from flask import Blueprint, request, make_response, abort
from backend.model.user import User
from backend.model.user_dao import create_user, select_user, select_all

blueprint = Blueprint("auth", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form["password"]

    all_users = select_all()

    print(all_users)

    for user in all_users:
        if user.get("username") == username and user.get("password") == password:
            response = make_response("success")
            response.set_cookie("user_id", str(user.get("userID")),  max_age=60*60*24*365*2)
            return response

    abort(404)


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

    user = User(username, password)

    user.set_email(email)
    user.set_firstname(firstname)
    user.set_lastname(lastname)
    user.set_age(int(age))
    user.set_hobby(hobby)
    user.set_acc_status(acc_status)

    create_user(user)

    return "successful"
