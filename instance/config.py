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
