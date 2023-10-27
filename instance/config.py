import os
from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.getenv('DEFAULT_SECRET_KEY')
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
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