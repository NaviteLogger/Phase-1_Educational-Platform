import os
from dotenv import load_dotenv

class Config:
    # The base directory of the project
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # Databace connection (common to all environments)
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_PORT = os.getenv('MYSQL_PORT')
    SECRET_KEY = os.getenv('DEFAULT_SECRET_KEY')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    # Development-specific configuration
    MYSQL_DB = os.getenv('MYSQL_DB')
    SECRET_KEY = os.getenv('DEV_SECRET_KEY')
    DEBUG = True
    TESTING = True

class TestingConfig(Config):
    SECRET_KEY = os.getenv('TEST_SECRET_KEY')
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    SECRET_KEY = os.getenv('PROD_SECRET_KEY')
    DEBUG = False
    TESTING = False