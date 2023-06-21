from flask import Blueprint, request
from backend.model.user_dao import select_all, select_user

blueprint = Blueprint("user_actions", __name__)


@blueprint.route("/get-all", methods=["POST"])
def get_all_users():
    all_users = select_all()
    return all_users


@blueprint.route("/select-user", methods=["POST"])
def select_user():
    user_id = request.form["userID"]
    user = select_user(int(user_id))
    return user

