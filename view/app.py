#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
from view.routes import views
import os


myapp = Flask(__name__)
cors = CORS(myapp, resources={r"/*": {"origin": "*"}})

def create_myapp():
    """Initialize the flask myapp"""
    myapp.register_blueprint(views)
    return myapp


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    myapp = create_myapp()
    myapp.run(port=port, host=host)
