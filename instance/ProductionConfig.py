import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PROD_SECRET_KEY = os.getenv('PROD_SECRET_KEY')

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_PASSWORD_PROD = os.getenv('MYSQL_PASSWORD_PROD')
MYSQL_DB_PROD = os.getenv('MYSQL_DB_PROD')
MYSQL_USER_PROD = os.getenv('MYSQL_USER_PROD')

SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER_PROD}:{MYSQL_PASSWORD_PROD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_PROD}?ssl-mode=REQUIRED'