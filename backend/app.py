from flask import Flask
from connect import connect_database
from model import user_dao
from controller.auth import blueprint as auth
from controller.friendship import blueprint as friendship

app = Flask(__name__)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(friendship, url_prefix="/friendship")

@app.route('/')
def test():
    # result = connect_database(
    #     "INSERT INTO User (username, password, firstname, lastname, age, hobby, accStatus) VALUES (?, ?, ?, ?, ?, ?, ?)",
    #     "user2", "1234", "test", "user2", "15", "griddy", "activated"
    # )

    return user_dao.select_all()

if __name__ == '__main__':
    app.run()

