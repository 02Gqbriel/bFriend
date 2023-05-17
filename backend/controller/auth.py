from flask import Blueprint, request

blueprint = Blueprint("auth", __name__)


@blueprint.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form["password"]
    return {'message: login successful'}
