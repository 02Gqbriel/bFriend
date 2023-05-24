from flask import Blueprint, request
from backend.model.user import User
from backend.model.user_dao import create_user

blueprint = Blueprint("auth", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    

    return {'message: login successful'}


@blueprint.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form["password"]
    return {'message: login successful'}
