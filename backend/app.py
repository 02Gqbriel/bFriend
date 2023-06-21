from flask import Flask, render_template

from controller.user_actions import blueprint as user_actions
from controller.auth import blueprint as auth
from controller.friendship import blueprint as friendship
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(friendship, url_prefix="/friendship")
app.register_blueprint(user_actions, url_prefix="/user_actions")


@app.route('/')
def red_login():
    return "good"

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:4200"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    return response


if __name__ == '__main__':
    app.run()
