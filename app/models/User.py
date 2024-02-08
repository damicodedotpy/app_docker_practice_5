from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import validators

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    
    @validates("email")
    def validateEmail(self, key, email):
        assert validators.email(email)
        return email

    def __repr__(self):
        return f"<User {self.username}>"