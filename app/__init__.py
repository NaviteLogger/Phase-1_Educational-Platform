import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the extensions here, outside of the create_app function
db = SQLAlchemy()
login_manager = LoginManager()

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
    app = Flask(__name__, instance_relative_config=True) # The instance_relative_config argument tells Flask that configuration files are relative to the instance folder, which is a location Flask provides to safely store instance-specific resources

    # Default config
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY')
    )

    # Load the instance config, if it exists, with testing configuration
    if app.config['ENV'] == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif app.config['ENV'] == 'testing':
        app.config.from_object('config.TestingConfig')
    elif app.config['ENV'] == 'production':
        app.config.from_object('config.ProductionConfig')

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register the blueprints
    from . import auth
    app.register_blueprint(auth.bp)

    return app