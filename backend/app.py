from flask import Flask
from controller import auth

app = Flask(__name__)

app.add_url_rule("/api/auth/login", "login", auth_func=auth.login)


if __name__ == '__main__':
    app.run()
