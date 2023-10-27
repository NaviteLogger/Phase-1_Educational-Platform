import os
from dotenv import load_dotenv

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

class TestingConfig(Config):
    # Testing-specific configuration
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    # Production-specific configuration
    DEBUG = False
    TESTING = False