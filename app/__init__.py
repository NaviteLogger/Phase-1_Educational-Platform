import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import FlaskLogin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
