import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TEST_SECRET_KEY = os.getenv('TEST_SECRET_KEY')

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_PASSWORD_TEST = os.getenv('MYSQL_PASSWORD_TEST')
MYSQL_DB_TEST = os.getenv('MYSQL_DB_TEST')
MYSQL_USER_TEST = os.getenv('MYSQL_USER_TEST')

SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER_TEST}:{MYSQL_PASSWORD_TEST}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_TEST}?ssl-mode=REQUIRED'