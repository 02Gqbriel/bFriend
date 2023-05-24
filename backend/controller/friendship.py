from flask import Blueprint

blueprint = Blueprint("friendship", __name__)


@blueprint.route("/create", methods=["POST"])
def create():

    return {'message: login successful'}


@blueprint.route("/list", methods=["GET"])
def read_many():

    return {'message: login successful'}


@blueprint.route("/read", methods=["GET"])
def read():

    return {'message: login successful'}


@blueprint.route("/update", methods=["PUT"])
def update():

    return {'message: login successful'}


@blueprint.route("/delete", methods=["DELETE"])
def delete():

    return {'message: login successful'}
