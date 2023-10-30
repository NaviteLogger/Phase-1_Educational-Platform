'''
This is the main file that will be used to run the application
'''
from  app import create_app, db

# Create the app instance
app = create_app()

if __name__ == '__main__':
    app.run()