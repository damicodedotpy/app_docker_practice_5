from flask_smorest import Blueprint
from models.User import User
from models.User import db
import os

blp = Blueprint("user", __name__, description="Operations on users")

@blp.route("/users", methods=["GET", "POST"])
def test():
    newUser = User(name="erik", lastname="torres", email="erik.torres@hotmail.com", password="1234")
    db.session.add(newUser)
    db.session.commit()
    return "New user created!"

