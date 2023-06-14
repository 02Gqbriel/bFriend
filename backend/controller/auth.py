from flask import Blueprint, request
from backend.model.user import User
from backend.model.user_dao import create_user, select_user

blueprint = Blueprint("auth", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form["password"]

    user = User(username, password)

    res = select_user(user.user_id)

    return "success"


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
