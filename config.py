# This is the config file that will link .env variables to the app.
import os

# The base directory of the project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# General config
SECRET_KEY = os.urandom(32) # Generate a random secret key
DEBUG = True

# MySQL database config
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')
MYSQL_PORT = os.getenv('MYSQL_PORT')