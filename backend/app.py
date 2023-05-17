from flask import Flask
from connect import connect_database
from controller.auth import blueprint as auth
from controller.friendship import blueprint as friendship

app = Flask(__name__)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(friendship, url_prefix="/friendship")


# app.add_url_rule("/api/auth/login", "login", auth.login)

@app.route('/')
def test():
    result = connect_database(
        "INSERT INTO User (username, password, firstname, lastname, age, hobby, accStatus) VALUES (?, ?, ?, ?, ?, ?, ?)",
        "testuser", "1234", "test", "user", "15", "fortnite", "activated"
    )
    return result


if __name__ == '__main__':
    app.run()
