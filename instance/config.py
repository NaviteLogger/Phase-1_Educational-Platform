import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # The base directory of the project
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('DEFAULT_SECRET_KEY')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    # Development-specific configuration
    DEBUG = True
    TESTING = True
    DEV_SECRET_KEY = os.getenv('DEV_SECRET_KEY')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_PORT = os.getenv('MYSQL_PORT')
    MYSQL_PASSWORD_DEV = os.getenv('MYSQL_PASSWORD_DEV')
    MYSQL_DB_DEV = os.getenv('MYSQL_DB_DEV')
    MYSQL_USER_DEV = os.getenv('MYSQL_USER_DEV')
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER_DEV}:{MYSQL_PASSWORD_DEV}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_DEV}?ssl-mode=REQUIRED'

class TestingConfig(Config):
    # Testing-specific configuration
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    # Production-specific configuration
    DEBUG = False
    TESTING = False