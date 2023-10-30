import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # The base directory of the project
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('DEFAULT_SECRET_KEY')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_PORT = os.getenv('MYSQL_PORT')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    # Development-specific configuration
    DEBUG = True
    TESTING = True
    DEV_SECRET_KEY = os.getenv('DEV_SECRET_KEY')
    MYSQL_PASSWORD_DEV = os.getenv('MYSQL_PASSWORD_DEV')
    MYSQL_DB_DEV = os.getenv('MYSQL_DB_DEV')
    MYSQL_USER_DEV = os.getenv('MYSQL_USER_DEV')
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER_DEV}:{MYSQL_PASSWORD_DEV}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{MYSQL_DB_DEV}?ssl-mode=REQUIRED'

class TestingConfig(Config):
    # Testing-specific configuration
    DEBUG = True
    TESTING = True
    TEST_SECRET_KEY = os.getenv('TEST_SECRET_KEY')
    MYSQL_PASSWORD_TEST = os.getenv('MYSQL_PASSWORD_TEST')
    MYSQL_DB_TEST = os.getenv('MYSQL_DB_TEST')
    MYSQL_USER_TEST = os.getenv('MYSQL_USER_TEST')
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER_TEST}:{MYSQL_PASSWORD_TEST}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{MYSQL_DB_TEST}?ssl-mode=REQUIRED'

class ProductionConfig(Config):
    # Production-specific configuration
    DEBUG = False
    TESTING = False
    PROD_SECRET_KEY = os.getenv('PROD_SECRET_KEY')
    MYSQL_PASSWORD_PROD = os.getenv('MYSQL_PASSWORD_PROD')
    MYSQL_DB_PROD = os.getenv('MYSQL_DB_PROD')
    MYSQL_USER_PROD = os.getenv('MYSQL_USER_PROD')
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER_PROD}:{MYSQL_PASSWORD_PROD}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{MYSQL_DB_PROD}?ssl-mode=REQUIRED'