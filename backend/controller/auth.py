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

    return {'message: login successful', res}


@blueprint.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form["password"]

    user = User(username, password)

    create_user(user)

    return {'message: register successful'}
