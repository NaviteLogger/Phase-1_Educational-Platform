# This is the main file that will be used to run the application
import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) # __name__ is the name of the current Python module