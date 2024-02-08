import os

from flask import Flask
from dotenv import load_dotenv

from routes.user import blp as userBlueprint
from models.User import db

load_dotenv()

def create_app():
    # Create the Flask app
    app = Flask(__name__)
    
    # App configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{os.getenv('POSTGRES_DATABASE_PASSWORD')}@host.docker.internal:5432/{os.getenv('POSTGRES_DATABASE_NAME')}"
    
    # Initialize the database
    db.init_app(app)
    
    # Register the blueprints
    app.register_blueprint(userBlueprint)
    
    # Create the database tables
    with app.app_context():
        db.create_all()
    

    return app