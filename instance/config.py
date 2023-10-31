import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # The base directory of the project
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('DEFAULT_SECRET_KEY')
    POSTGRESQL_HOST = os.getenv('POSTGRESQL_HOST')
    POSTGRESQL_PORT = os.getenv('POSTGRESQL_PORT')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    # Development-specific configuration
    DEBUG = True
    TESTING = True
    DEV_SECRET_KEY = os.getenv('DEV_SECRET_KEY')
    POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
    POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
    POSTGRESQL_DATABASE = os.getenv('POSTGRESQL_DATABASE')
    POSTGRESQL_SSLMODE = os.getenv('POSTGRESQL_SSLMODE')
    POSTGRESQL_URI = f"postgresql+psycopg2://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{Config.POSTGRESQL_HOST}:{Config.POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}?sslmode={POSTGRESQL_SSLMODE}&sslrootcert=./ca-certificate.crt"


class TestingConfig(Config):
    # Testing-specific configuration
    DEBUG = True
    TESTING = True
    TEST_SECRET_KEY = os.getenv('TEST_SECRET_KEY')


class ProductionConfig(Config):
    # Production-specific configuration
    DEBUG = False
    TESTING = False
    PROD_SECRET_KEY = os.getenv('PROD_SECRET_KEY')
