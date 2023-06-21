from flask import Blueprint, request

from backend.model.user import User
from backend.model.user_dao import select_all, select_user, delete_user, update_user

blueprint = Blueprint("user_actions", __name__)


@blueprint.route("/get-all", methods=["POST"])
def get_all_users():
    all_users = select_all()
    return all_users


@blueprint.route("/select-user", methods=["POST"])
def select_user_from_database():
    user_id = request.form["userID"]
    user = select_user(int(user_id))
    return user


@blueprint.route("/delete-user", methods=["POST"])
def delete_user_from_database():
    user_id = request.form["userID"]
    response = delete_user(int(user_id))
    return response


@blueprint.route("/edit-user", methods=["POST"])
def update_user_from_database():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    age = request.form['age']
    hobby = request.form['hobby']

    user = User(username, password)

    user.set_email(email)
    user.set_firstname(firstname)
    user.set_lastname(lastname)
    user.set_age(int(age))
    user.set_hobby(hobby)

    update_user(user, 1)
    return "Deleted"
