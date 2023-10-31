import os
from flask import Flask
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

'''
The "Application Factory" (in this case the 'create_app' function) is a 
pattern in Flask where the application is created inside a function,
allowing for different instances of the app to be created with different 
configurations. This is particularly useful for:
- Configuring applications differently for different environments (development, testing, production, etc.)
- Ensuring that resources (like databases) are correctly set up every time an app instance is created.
- Facilitating unit testing by easily allowing the creation of a fresh app instance for each test.
'''
def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Set the default config file
    env = os.environ.get('FLASK_ENV', 'production') # Default to production

    # Load the selected config file
    if os.environ.get('FLASK_ENV') == 'development':
        app.config.from_object('instance.config.DevelopmentConfig')
        # ...
    elif os.environ.get('FLASK_ENV') == 'testing':
        app.config.from_object('instance.config.TestingConfig')
        # ...
    elif os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object('instance.config.ProductionConfig')
        # ...

    # Establish a connection to the database
    engine = create_engine(app.config['POSTGRESQL_URI'])

    # Test the database connection
    connection = engine.connect()
    result = connection.execute(text("SELECT 1"))
    data = result.fetchall()
    print(data)

    return app