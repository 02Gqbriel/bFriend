from flask import Flask
from connect import connect_database
from controller.auth import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint, url_prefix="/auth")


# app.add_url_rule("/api/auth/login", "login", auth.login)

@app.route('/')
def test():
    return connect_database(
        "INSERT INTO User (username, password, firstname, lastname, hobby, accStatus) VALUES (?, ?, ?, ?, ?, ?)",
        "testuser", "1234", "test", "user", "fortnite", "activated")


if __name__ == '__main__':
    app.run()
