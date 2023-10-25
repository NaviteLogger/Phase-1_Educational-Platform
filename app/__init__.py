import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the extensions here, outside of the create_app function
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Default config
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY')
    )

    # Load the instance config, if it exists, when not testing
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)