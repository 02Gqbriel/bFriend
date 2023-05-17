from flask import Flask
from connect import connect_database
from controller.auth import blueprint


app = Flask(__name__)

app.add_url_rule("/api/auth/login", "login", auth_func=auth.login)


if __name__ == '__main__':
    app.run()

