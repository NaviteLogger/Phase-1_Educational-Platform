'''
The __init__.py file is required to treat the main directory as a Python package.
Also, the '__init__.py' file in each folder will typically be used to create a
Blueprint for that particulare module. This allows us to define the routes specific
to that module in the module's __init__.py file.
'''

from flask import Blueprint

main = Blueprint('main', __name__)

from . import routes
