from flask import render_template
from . import main

# Handle GET requests for the root URL
@main.route('/')
def index():
    return render_template('index.html')