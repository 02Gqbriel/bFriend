from flask import Blueprint, request
from backend.model.user_dao import select_all

blueprint = Blueprint("auth", __name__)


@blueprint.route("/get-all", methods=["POST"])
def get_all_users():
    all_users = select_all()
    return all_users
